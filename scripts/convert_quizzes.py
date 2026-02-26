"""
Script para converter automaticamente todos os quizzes de markdown para HTML interativo
"""
import pathlib
import re
import yaml
from rich import print
from rich.progress import track


def get_site_name():
    """Lê o nome do site do mkdocs.yml"""
    try:
        with open('mkdocs.yml', 'r', encoding='utf-8') as f:
            config = yaml.load(f, Loader=yaml.UnsafeLoader)
            return config.get('site_name', 'Curso')
    except Exception:
        return 'Curso'

SITE_NAME = get_site_name()

def parse_quiz_markdown(content: str) -> list:
    """Extrai perguntas e opções do markdown"""
    questions = []
    
    # Dividir por blocos de perguntas (número seguido de ponto)
    blocks = re.split(r'\n(?=\d+\.\s+\*\*)', content)
    
    for block in blocks:
        # Extrair pergunta
        q_match = re.search(r'(\d+)\.\s+\*\*(.*?)\*\*', block)
        if not q_match:
            continue
            
        q_num = q_match.group(1)
        q_text = q_match.group(2).strip()
        
        # Extrair opções
        options = []
        option_lines = re.findall(r'^\s*\*\s+\((.*?)\)\s+(.*)', block, re.MULTILINE)
        
        for marker, text in option_lines:
            # Remover explicação da linha da opção se houver
            clean_text = re.sub(r'\*Explicação:.*', '', text).strip()
            if clean_text:
                options.append({
                    'correct': marker.lower() == 'x',
                    'text': clean_text
                })
            
        if options:
            questions.append({
                'number': q_num,
                'text': q_text,
                'options': options
            })
    
    return questions

def generate_quiz_html(quiz_number: int, questions: list, quiz_title: str) -> str:
    """Gera HTML completo do quiz"""
    # Limpar títulos de sufixos fixos
    clean_title = re.sub(r' - Introdução$', '', quiz_title)
    
    html_parts = [
        f"# {clean_title}\n",
        '\n--8<-- "assets/quiz.html"\n\n'
    ]
    
    # Gerar cada pergunta
    for q in questions:
        html_parts.append('<div class="quiz-container">\n')
        html_parts.append(f'  <div class="quiz-question">{q["number"]}. {q["text"]}</div>\n')
        
        for opt in q['options']:
            correct_attr = 'true' if opt['correct'] else 'false'
            feedback = f"✅ Correto! {opt['text']}" if opt['correct'] else f"Incorreto. Tente novamente."
            
            html_parts.append(
                f'  <div class="quiz-option" data-correct="{correct_attr}" '
                f'data-feedback="{feedback}">{opt["text"]}</div>\n'
            )
        
        html_parts.append('  <div class="quiz-feedback"></div>\n')
        html_parts.append('</div>\n\n')
    
    return ''.join(html_parts)


def convert_quiz(quiz_path: pathlib.Path) -> bool:
    """Converte um arquivo de quiz"""
    try:
        content = quiz_path.read_text(encoding='utf-8')
        
        # Extrair título real do arquivo se disponível, senão padrão
        title_match = re.search(r'# (.*)', content)
        if title_match:
            quiz_title = title_match.group(1)
        else:
            num_match = re.search(r'quiz-(\d+)', quiz_path.name)
            quiz_title = f"Quiz {num_match.group(1)}" if num_match else "Quiz"
        
        # Parse perguntas
        questions = parse_quiz_markdown(content)
        
        if not questions:
            print(f"  [yellow]⚠[/yellow] Nenhuma pergunta encontrada em {quiz_path.name}")
            return False
        
        # Extrair número do quiz
        quiz_num = int(re.search(r'quiz-(\d+)', quiz_path.name).group(1))
        
        # Gerar HTML
        html_content = generate_quiz_html(quiz_num, questions, quiz_title)
        
        # Salvar em docs/quizzes (um nível acima de src)
        output_path = quiz_path.parent.parent / quiz_path.name
        output_path.write_text(html_content, encoding='utf-8')
        
        print(f"  [green]✓[/green] Converteu {quiz_path.name} -> {output_path} ({len(questions)} perguntas)")
        return True
        
    except Exception as e:
        print(f"  [red]✗[/red] Erro em {quiz_path.name}: {e}")
        return False


def convert_all_quizzes():
    """Converte todos os quizzes"""
    # Usar pasta .src como fonte
    quizzes_src_dir = pathlib.Path('docs/quizzes/src')
    
    if not quizzes_src_dir.exists():
        print(f"[yellow]⚠ Pasta {quizzes_src_dir} não encontrada.[/yellow]")
        return
    
    print(f"\n[bold cyan]🧠 Convertendo Quizzes para {SITE_NAME}...[/bold cyan]")
    print(f"Fonte: {quizzes_src_dir}")
    
    quiz_files = sorted(quizzes_src_dir.glob('quiz-*.md'))
    
    if not quiz_files:
        print(f"[yellow]⚠ Nenhum arquivo de quiz encontrado em {quizzes_src_dir}[/yellow]")
        return
    
    converted = 0
    for quiz_path in track(quiz_files, description="Processando quizzes..."):
        if convert_quiz(quiz_path):
            converted += 1
    
    print(f"\n[green]✓ {converted}/{len(quiz_files)} quizzes convertidos com sucesso![/green]")


def main():
    """Função principal"""
    print(f"[bold]🚀 Conversão Automática de Quizzes: {SITE_NAME}[/bold]")
    print("=" * 50)
    
    convert_all_quizzes()
    
    print("\n[green]✅ Conversão concluída![/green]")


if __name__ == '__main__':
    main()
