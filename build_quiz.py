from pathlib import Path
from textwrap import dedent

root = Path(__file__).resolve().parent

index_html = dedent('''
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>QR Code Quest</title>
  <style>
    :root {
      --bg: #07111f;
      --line: rgba(148, 163, 184, 0.18);
      --text: #e2e8f0;
      --muted: #a5b4cf;
      --cyan: #4dd0e1;
      --blue: #60a5fa;
      --purple: #a78bfa;
      --green: #34d399;
      --shadow: rgba(15, 23, 42, 0.7);
    }
    * { box-sizing: border-box; }
    html, body { margin: 0; min-height: 100%; }
    body {
      min-height: 100vh;
      display: grid;
      place-items: center;
      padding: 24px;
      font-family: Arial, Helvetica, sans-serif;
      background: radial-gradient(circle at top, rgba(96,165,250,.22), transparent 20%), radial-gradient(circle at bottom, rgba(167,139,250,.22), transparent 18%), linear-gradient(180deg, #020817 0%, var(--bg) 100%);
      color: var(--text);
    }
    .shell {
      width: min(1100px, 100%);
      border: 1px solid var(--line);
      border-radius: 28px;
      background: rgba(8, 15, 27, 0.78);
      box-shadow: 0 30px 80px var(--shadow);
      overflow: hidden;
    }
    .header {
      padding: 26px 28px 18px;
      background: linear-gradient(180deg, rgba(15, 23, 42, 0.8), rgba(15, 23, 42, 0.2));
      border-bottom: 1px solid var(--line);
    }
    .title {
      margin: 0;
      font-size: clamp(2rem, 4vw, 3.2rem);
      letter-spacing: .08em;
      text-transform: uppercase;
      color: #f8fafc;
    }
    .subtitle {
      margin: 10px 0 0;
      color: var(--muted);
      font-size: 1.06rem;
      line-height: 1.7;
    }
    .content {
      display: grid;
      grid-template-columns: 1.1fr 1.9fr;
      gap: 24px;
      padding: 28px;
    }
    .intro-card, .level-grid {
      background: rgba(15, 23, 42, 0.8);
      border: 1px solid var(--line);
      border-radius: 22px;
      padding: 24px;
    }
    .intro-card h2 {
      margin: 0 0 12px;
      font-size: 1.3rem;
      color: #f8fafc;
    }
    .intro-card p {
      margin: 0;
      color: var(--muted);
      line-height: 1.7;
    }
    .level-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 18px;
    }
    .card-level {
      display: block;
      text-decoration: none;
      color: var(--text);
      background: linear-gradient(180deg, rgba(15, 23, 42, 0.85), rgba(19, 32, 52, 0.95));
      border: 1px solid rgba(96, 165, 250, 0.25);
      border-radius: 18px;
      padding: 18px 16px;
      transition: transform .2s ease, border-color .2s ease, box-shadow .2s ease;
    }
    .card-level:hover {
      transform: translateY(-3px);
      border-color: rgba(94, 234, 212, 0.7);
      box-shadow: 0 20px 30px rgba(59, 130, 246, 0.14);
    }
    .level-badge {
      display: inline-block;
      padding: 6px 10px;
      border-radius: 999px;
      font-size: .72rem;
      letter-spacing: .08em;
      text-transform: uppercase;
      background: rgba(125, 211, 252, 0.12);
      color: var(--cyan);
      border: 1px solid rgba(125, 211, 252, 0.2);
    }
    .card-level h3 {
      margin: 14px 0 8px;
      font-size: 1.15rem;
    }
    .card-level p {
      margin: 0;
      color: var(--muted);
      line-height: 1.5;
      font-size: .95rem;
    }
    @media (max-width: 760px) {
      .content { grid-template-columns: 1fr; }
      .shell { border-radius: 20px; }
      .header { padding: 22px 20px 12px; }
      .content { padding: 20px; }
      .intro-card, .level-grid { padding: 18px; }
    }
  </style>
</head>
<body>
  <div class="shell">
    <header class="header">
      <h1 class="title">QR Code Quest</h1>
      <p class="subtitle">5 fases de múltipla escolha sobre computação. Comece pelo nível mais fácil e avance até o desafio final.</p>
    </header>
    <main class="content">
      <section class="intro-card">
        <h2>Missão</h2>
        <p>Resolva as 5 perguntas de computação e marque pontuação máxima. Cada fase aumenta o nível de dificuldade.</p>
      </section>
      <section class="level-grid" aria-label="Lista das fases do jogo">
        <a class="card-level" href="atomo.html">
          <span class="level-badge">Nível 1</span>
          <h3>Introdução</h3>
          <p>Estruturas básicas e conceitos iniciais.</p>
        </a>
        <a class="card-level" href="foton.html">
          <span class="level-badge">Nível 2</span>
          <h3>Fundamentos</h3>
          <p>Sistema operacional e funcionamento do computador.</p>
        </a>
        <a class="card-level" href="genoma.html">
          <span class="level-badge">Nível 3</span>
          <h3>Web</h3>
          <p>HTML, CSS e a linguagem da internet.</p>
        </a>
        <a class="card-level" href="quasar.html">
          <span class="level-badge">Nível 4</span>
          <h3>Algoritmos</h3>
          <p>Complexidade e lógica de busca.</p>
        </a>
        <a class="card-level" href="higgs.html">
          <span class="level-badge">Nível 5</span>
          <h3>Final</h3>
          <p>Conceitos avançados de redes e comunicação.</p>
        </a>
      </section>
    </main>
  </div>
</body>
</html>
''')

page_template = '''
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <style>
    :root {{
      --bg: #07111f; --panel: rgba(15, 23, 42, 0.9); --line: rgba(148, 163, 184, 0.18); --text: #e2e8f0; --muted: #a5b4cf; --cyan: #67e8f9; --blue: #60a5fa; --purple: #a78bfa; --green: #34d399; --red: #f87171;
    }}
    * {{ box-sizing: border-box; }}
    html, body {{ margin: 0; min-height: 100%; }}
    body {{
      min-height: 100vh; display: grid; place-items: center; padding: 24px; font-family: Arial, Helvetica, sans-serif; background: radial-gradient(circle at top left, rgba(96, 165, 250, 0.23), transparent 18%), radial-gradient(circle at bottom right, rgba(167, 139, 250, 0.24), transparent 16%), linear-gradient(180deg, #020817, var(--bg)); color: var(--text);
    }}
    .shell {{ width: min(960px, 100%); background: rgba(8, 15, 27, 0.8); border: 1px solid var(--line); border-radius: 26px; box-shadow: 0 26px 72px rgba(15, 23, 42, 0.7); overflow: hidden; }}
    .topbar {{ display: flex; justify-content: space-between; align-items: center; gap: 16px; padding: 18px 22px; border-bottom: 1px solid var(--line); background: rgba(15, 23, 42, 0.7); }}
    .tag {{ display: inline-flex; align-items: center; border-radius: 999px; padding: 8px 12px; background: rgba(16, 185, 129, 0.12); border: 1px solid rgba(16, 185, 129, 0.22); color: var(--green); font-size: 0.78rem; letter-spacing: .12em; text-transform: uppercase; font-weight: 700; }}
    .level {{ color: var(--muted); font-size: 0.85rem; font-weight: 700; letter-spacing: .08em; text-transform: uppercase; }}
    .content {{ padding: 24px; }}
    .question-panel {{ background: rgba(15, 23, 42, 0.85); border: 1px solid var(--line); border-radius: 22px; padding: 22px; }}
    .label {{ display: inline-block; margin-bottom: 10px; color: var(--cyan); letter-spacing: .12em; text-transform: uppercase; font-size: .72rem; font-weight: 700; }}
    .question-panel h1 {{ margin: 0 0 18px; font-size: clamp(1.4rem, 3vw, 2.2rem); line-height: 1.4; color: #f8fafc; }}
    .options {{ display: grid; grid-template-columns: 1fr; gap: 12px; margin-top: 20px; }}
    .option {{ width: 100%; border: 1px solid rgba(148, 163, 184, 0.22); background: rgba(30, 41, 59, 0.8); color: var(--text); border-radius: 14px; padding: 14px 16px; text-align: left; font-size: 1rem; cursor: pointer; transition: transform .18s ease, border-color .18s ease, background .18s ease; }}
    .option:hover {{ transform: translateY(-1px); border-color: rgba(96, 165, 250, 0.6); background: rgba(37, 99, 235, 0.12); }}
    .option.correct {{ background: rgba(16, 185, 129, 0.2); border-color: rgba(52, 211, 153, 0.9); color: #d1fae5; }}
    .option.wrong {{ background: rgba(248, 113, 113, 0.14); border-color: rgba(248, 113, 113, 0.8); color: #fee2e2; }}
    .feedback {{ min-height: 56px; margin-top: 18px; border-radius: 14px; padding: 14px 16px; font-size: 1rem; line-height: 1.5; background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(148, 163, 184, 0.14); color: var(--muted); }}
    .feedback.success {{ background: rgba(16, 185, 129, 0.12); border-color: rgba(16, 185, 129, 0.5); color: #d1fae5; }}
    .feedback.error {{ background: rgba(248, 113, 113, 0.12); border-color: rgba(248, 113, 113, 0.5); color: #fee2e2; }}
    .actions {{ display: flex; justify-content: space-between; gap: 12px; margin-top: 22px; }}
    .btn {{ display: inline-flex; align-items: center; justify-content: center; text-decoration: none; border-radius: 999px; padding: 12px 18px; font-weight: 700; border: 1px solid transparent; cursor: pointer; transition: transform .18s ease, opacity .18s ease; }}
    .btn:hover {{ transform: translateY(-1px); }}
    .btn.secondary {{ background: rgba(148, 163, 184, 0.1); color: var(--text); border-color: rgba(148, 163, 184, 0.18); }}
    .btn.primary {{ background: linear-gradient(135deg, var(--blue), var(--purple)); color: #eff6ff; box-shadow: 0 10px 26px rgba(96, 165, 250, 0.28); }}
    @media (max-width: 720px) {{ .topbar {{ flex-direction: column; align-items: flex-start; }} .shell {{ border-radius: 20px; }} .content {{ padding: 18px; }} .question-panel {{ padding: 18px; }} }}
  </style>
</head>
<body>
  <div class="shell">
    <div class="topbar">
      <div class="tag">QR-{level}</div>
      <div class="level">{level_text}</div>
    </div>
    <main class="content">
      <div class="question-panel">
        <span class="label">Pergunta</span>
        <h1>{question}</h1>
        <div class="options" id="options"></div>
        <div class="feedback" id="feedback">Escolha uma alternativa para responder.</div>
        <div class="actions">
          <a href="index.html" class="btn secondary">Menu</a>
          <a id="nextBtn" href="{next_page}" class="btn primary" style="display:none;">Próxima fase</a>
        </div>
      </div>
    </main>
  </div>
  <script>
    const options = {choices};
    const correctIndex = {correct_index};
    const attemptKey = 'qr-quest:failed:' + window.location.pathname;
    let failedAnswer = localStorage.getItem(attemptKey);
    const nextBtn = document.getElementById('nextBtn');
    const feedback = document.getElementById('feedback');
    const optionRoot = document.getElementById('options');
    const buttons = options.map((text, index) => {{
      const button = document.createElement('button');
      button.type = 'button';
      button.className = 'option';
      button.textContent = `${{index + 1}}. ${{text}}`;
      button.addEventListener('click', () => {{
        if (failedAnswer !== null) return;
        const isCorrect = index === correctIndex;
        buttons.forEach((btn, btnIndex) => {{
          btn.disabled = true;
          btn.classList.remove('correct', 'wrong');
          if (btnIndex === correctIndex) btn.classList.add('correct');
          if (btnIndex === index && !isCorrect) btn.classList.add('wrong');
        }});
        if (isCorrect) {{
          feedback.textContent = '✅ Correto! Você desbloqueou a próxima etapa.';
          feedback.className = 'feedback success';
        }} else {{
          failedAnswer = String(index);
          localStorage.setItem(attemptKey, failedAnswer);
          feedback.textContent = `❌ Errado. A resposta certa é: ${{options[correctIndex]}}.`;
          feedback.className = 'feedback error';
        }}
        if (isCorrect) nextBtn.style.display = 'inline-flex';
      }});
      return button;
    }});
    optionRoot.append(...buttons);
    if (failedAnswer !== null) {{
      buttons.forEach((button, index) => {{
        button.disabled = true;
        if (index === correctIndex) button.classList.add('correct');
        if (index === Number(failedAnswer)) button.classList.add('wrong');
      }});
      feedback.textContent = `❌ Você já errou esta pergunta. A resposta certa é: ${{options[correctIndex]}}.`;
      feedback.className = 'feedback error';
    }}
  </script>
</body>
</html>
'''

questions = [
    {
        'file': 'atomo.html',
        'level': '01',
        'level_text': 'Nível 1 · Fácil',
        'question': 'Qual estrutura de dados armazena elementos em sequência e permite acesso pelo índice?',
        'choices': ['Array', 'Árvore', 'HashMap', 'Pilha'],
        'correct_index': 0,
        'next_page': 'foton.html',
    },
    {
        'file': 'foton.html',
        'level': '02',
        'level_text': 'Nível 2 · Intermediário',
        'question': 'Qual é a principal função de um sistema operacional?',
        'choices': ['Processar imagens 3D', 'Gerenciar recursos do computador e executar programas', 'Criar páginas web', 'Compilar código em linguagem de máquina'],
        'correct_index': 1,
        'next_page': 'genoma.html',
    },
    {
        'file': 'genoma.html',
        'level': '03',
        'level_text': 'Nível 3 · Intermediário',
        'question': 'Qual linguagem é usada principalmente para definir a estrutura e o conteúdo de uma página web?',
        'choices': ['CSS', 'JavaScript', 'HTML', 'SQL'],
        'correct_index': 2,
        'next_page': 'quasar.html',
    },
    {
        'file': 'quasar.html',
        'level': '04',
        'level_text': 'Nível 4 · Difícil',
        'question': 'Qual é a complexidade de tempo de uma busca binária em um vetor com n elementos?',
        'choices': ['O(1)', 'O(log n)', 'O(n)', 'O(n²)'],
        'correct_index': 1,
        'next_page': 'higgs.html',
    },
    {
        'file': 'higgs.html',
        'level': '05',
        'level_text': 'Nível 5 · Muito difícil',
        'question': 'Qual protocolo da camada de transporte é responsável por garantir entrega confiável de dados entre hosts?',
        'choices': ['UDP', 'HTTP', 'TCP', 'FTP'],
        'correct_index': 2,
        'next_page': 'index.html',
    },
]

for item in questions:
    html = page_template.format(
        title=f"QR {item['level']}",
        level=item['level'],
        level_text=item['level_text'],
        question=item['question'],
        choices=repr(item['choices']),
        correct_index=item['correct_index'],
        next_page=item['next_page'],
    )
    (root / item['file']).write_text(html, encoding='utf-8')

(root / 'index.html').write_text(index_html, encoding='utf-8')
(root / 'README.md').write_text(
    "# QR Code Quest\n\nJogo estático de perguntas de múltipla escolha sobre computação, com 5 níveis do mais fácil para o mais difícil.\n\n## Como abrir\n\nAbra o arquivo index.html em um navegador, ou rode um servidor local:\n\n```bash\npython -m http.server 8000\n```\n\nDepois acesse http://localhost:8000\n",
    encoding='utf-8',
)

print('Updated', len(questions) + 1, 'files')
