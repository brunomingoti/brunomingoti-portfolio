# brunomingoti-portfolio

Portfólio pessoal de Bruno Mingoti — site bilíngue (PT/EN) com projetos, publicações, experiência e contato.

## Arquitetura

- `backend/` — Django, usado **apenas localmente** como painel de administração de conteúdo (projetos, publicações, experiência, educação). Não é hospedado; serve só para editar o conteúdo com conforto (admin do Django) em vez de mexer em JSON à mão.
- `frontend/` — Vite + React + TypeScript. É um site **100% estático**: consome `frontend/src/data/content.json` (gerado a partir do Django) e é publicado no GitHub Pages via GitHub Actions a cada push na `main`.

```
backend (Django admin, SQLite) --export_content--> frontend/src/data/content.json --vite build--> GitHub Pages
```

## Editar conteúdo

1. Ative o virtualenv e rode o admin:
   ```bash
   source .venv/Scripts/activate
   cd backend
   python manage.py runserver
   ```
2. Acesse `http://localhost:8000/admin` (crie um superusuário com `python manage.py createsuperuser` se ainda não tiver um) e edite projetos, publicações, experiência, educação ou o perfil.
3. Exporte o conteúdo atualizado para o frontend:
   ```bash
   python manage.py export_content
   ```
4. Se adicionar imagens de projeto pelo admin, copie a pasta `backend/media/` correspondente para `frontend/public/media/` antes de buildar (o export já referencia os caminhos `/media/...`).
5. Rode `git add`, commit e push — o GitHub Actions builda e publica automaticamente.

Para popular o banco novamente do zero com o conteúdo original do currículo: `python manage.py seed_content`.

## Rodar o frontend localmente

```bash
cd frontend
npm install
npm run dev
```

## Deploy

Publicado via GitHub Actions (`.github/workflows/deploy.yml`) em GitHub Pages a cada push na branch `main`. Habilite Pages no repositório em Settings → Pages → Source → GitHub Actions.

URL esperada: `https://brunomingoti.github.io/brunomingoti-portfolio/`
