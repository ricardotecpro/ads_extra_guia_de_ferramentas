document.addEventListener("DOMContentLoaded", function () {
    // 1. Encontrar todos os comentários <!-- termynal -->
    const iterator = document.createNodeIterator(
        document.body,
        NodeFilter.SHOW_COMMENT,
        { acceptNode: (node) => node.nodeValue.trim() === 'termynal' ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT }
    );

    const termyDivs = [];
    let comment;
    while (comment = iterator.nextNode()) {
        const nextEl = comment.nextElementSibling;
        if (nextEl && (nextEl.classList.contains('highlight') || nextEl.tagName === 'PRE')) {
            termyDivs.push(nextEl);
            nextEl.classList.add('termy');
        }
    }

    // 2. Também buscar por classes explicitas .termy (legado)
    const directTermys = document.querySelectorAll(".termy");
    directTermys.forEach(d => { if (!termyDivs.includes(d)) termyDivs.push(d); });

    console.log("Found termynals for enhancement:", termyDivs.length);

    termyDivs.forEach(termynal => {
        const addCopyButton = () => {
            if (termynal.querySelector('.termynal-copy-button')) return;

            const button = document.createElement("button");
            button.className = "termynal-copy-button";
            button.innerHTML = `
                <span class="termynal-copy-icon">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M19 21H8V7h11m0-2H8a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h11a2 2 0 0 0 2-2V7a2 2 0 0 0-2-2m-3-4H4a2 2 0 0 0-2 2v14h2V3h12V1z"/></svg>
                </span>
                <span class="termynal-copy-feedback">Copied!</span>
            `;
            button.setAttribute("aria-label", "Copy to clipboard");
            
            // Estilo básico para garantir visibilidade se o CSS falhar
            button.style.position = 'absolute';
            button.style.right = '10px';
            button.style.top = '10px';

            termynal.style.position = 'relative';
            termynal.appendChild(button);

            button.addEventListener("click", () => {
                const code = termynal.querySelector('code');
                let textToCopy = "";
                
                if (code) {
                    const lines = code.innerText.split('\n');
                    const filtered = lines.map(line => {
                        let t = line.trim();
                        if (t.startsWith('$ ')) return t.substring(2);
                        if (t.startsWith('C:\\> ')) return t.substring(4);
                        return t;
                    });
                    textToCopy = filtered.join('\n');
                } else {
                    textToCopy = termynal.innerText;
                }

                navigator.clipboard.writeText(textToCopy.trim()).then(() => {
                    button.classList.add("copied");
                    setTimeout(() => button.classList.remove("copied"), 2000);
                });
            });
        };

        addCopyButton();
    });
});
