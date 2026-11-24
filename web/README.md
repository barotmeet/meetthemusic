# ClassicalVerse — Static HTML/CSS/JS + Python (Flask)

Premium scholarly web app for Hindustani and Carnatic classical music. Plain HTML/CSS/JS frontend served by a small Flask Python backend that also exposes a JSON API for all 10 modules.

## Run locally

```bash
cd backend
pip install -r requirements.txt
python app.py
```

Then open http://localhost:5000

## Project layout

```
classicalverse/
├── backend/
│   ├── app.py              # Flask app: JSON API + static frontend server
│   ├── data.py             # Seeded data (ragas, bandishes, taals, …)
│   ├── build_pages.py      # Re-generates frontend HTML pages
│   └── requirements.txt
└── frontend/
    ├── index.html          # Landing page
    ├── css/styles.css      # Full design system (light/dark)
    ├── js/app.js           # Theme toggle, mobile menu, API fetch + render
    └── pages/
        ├── ragas.html      bandishes.html  taals.html
        ├── artists.html    gurus.html      concerts.html
        ├── learn.html      community.html  archive.html
        ├── knowledge.html  raga.html       (detail page, ?slug=yaman)
```

## API endpoints

| Endpoint                | Returns                              |
|-------------------------|--------------------------------------|
| `GET /api/modules`      | All 10 module summaries              |
| `GET /api/ragas`        | List of ragas                        |
| `GET /api/ragas/<slug>` | One raga + its bandishes             |
| `GET /api/bandishes`    | List of bandishes                    |
| `GET /api/taals`        | List of taals                        |
| `GET /api/artists`      | List of artists                      |
| `GET /api/gurus`        | List of gurus                        |
| `GET /api/concerts`     | Upcoming concerts                    |
| `GET /api/courses`      | Learning paths                       |
| `GET /api/community`    | Forum threads                        |
| `GET /api/archives`     | Archive items                        |

## Design

- Cormorant Garamond (serif) for headings, Inter (sans) for body
- Saffron-gold + midnight-ink palette; light & dark themes
- Theme preference persisted in `localStorage`
- Fully responsive, mobile-first, no build step required

## Extending

- Add new data in `backend/data.py`
- Re-generate pages with `python backend/build_pages.py`
- Plug a database into `data.py` later without changing the frontend
