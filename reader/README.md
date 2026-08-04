# F1 Time Capsule — reader

Statyczna czytelnia generowana z `archive/`. Odblokowuje dokumenty do punktu
z `archive-state.yaml` (granica spoiler-safe).

## Lokalnie (bez kont)

```bash
cd reader
pip install -r requirements.txt
python serve.py
```

Otworzy się `http://127.0.0.1:4321/`. Sam build:

```bash
python build.py
```

## W internecie (też bez nowego konta)

Wystarczy istniejące repo na GitHubie + **GitHub Pages**:

1. Push zmian (folder `reader/` + workflow).
2. GitHub → **Settings → Pages → Source: GitHub Actions**.
3. Adres po deployu:
   `https://iamdeveloperidevelop.github.io/F1-Time-Capsule/`

Żadnego Vercela / Netlify nie trzeba.
