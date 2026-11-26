#!/usr/bin/env python3
"""Generator halaman Language Classes (TIAS / Little Lab Stories).

Menghasilkan 3 halaman statis dari satu template:
  language-classes.html      (English, default)
  language-classes-id.html   (Bahasa Indonesia)
  language-classes-ru.html   (Русский)

Jalankan dari folder ini:  python3 build.py
Output ditulis ke folder deploy Vercel: "Little lab stories/".
"""
import os
import sys
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT_DIR = os.path.join(REPO, "Little lab stories")

WA_NUMBER = "6285921162228"
SITE = "https://www.littlelabstories.com"
PAGES = {
    "en": "language-classes.html",
    "id": "language-classes-id.html",
    "ru": "language-classes-ru.html",
}


def wa(text):
    return f"https://wa.me/{WA_NUMBER}?text={quote(text)}"


# --------------------------------------------------------------------------- sprite
SPRITE = """
<svg class="sprite" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false">
  <symbol id="i-globe" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3c2.6 2.7 2.6 15.3 0 18"/><path d="M12 3c-2.6 2.7-2.6 15.3 0 18"/></symbol>
  <symbol id="i-calendar" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="16" rx="2.5"/><path d="M8 3v4M16 3v4M3 10.5h18"/></symbol>
  <symbol id="i-spark" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M11 3.5l1.7 4.3 4.3 1.7-4.3 1.7L11 15.5 9.3 11.2 5 9.5l4.3-1.7z"/><path d="M18 14l.8 2.2 2.2.8-2.2.8L18 20l-.8-2.2-2.2-.8 2.2-.8z"/></symbol>
  <symbol id="i-chat" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.6a8.4 8.4 0 0 1-8.4 8.4H8.6L3 22.5l1.4-4.6A8.4 8.4 0 1 1 21 11.6z"/><path d="M8.5 11.5h.01M12 11.5h.01M15.5 11.5h.01"/></symbol>
  <symbol id="i-route" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M3.5 20h4v-4h4v-4h4V8h5"/><circle cx="3.5" cy="20" r="1.1" fill="currentColor" stroke="none"/><circle cx="20.5" cy="8" r="1.1" fill="currentColor" stroke="none"/></symbol>
  <symbol id="i-book" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 6.6C10.6 5.1 8.5 4.5 4 4.6v13c4.5-.1 6.6.5 8 2 1.4-1.5 3.5-2.1 8-2v-13c-4.5-.1-6.6.5-8 2z"/><path d="M12 6.6v13"/></symbol>
  <symbol id="i-chart" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20V11M10 20V5M16 20v-6M22 20H2"/></symbol>
  <symbol id="i-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h13"/><path d="M12.5 5.5L19 12l-6.5 6.5"/></symbol>
  <symbol id="i-user" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="3.6"/><path d="M4.5 20a7.5 7.5 0 0 1 15 0"/></symbol>
  <symbol id="i-users" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="8.2" r="3.2"/><path d="M2.6 19.5a6.6 6.6 0 0 1 12.8 0"/><path d="M16.4 5.4a3.2 3.2 0 0 1 0 5.8"/><path d="M18 19.5a6.2 6.2 0 0 0-2-4.4"/></symbol>
  <symbol id="i-smile" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M8.4 14.3c.9 1.2 2.1 1.9 3.6 1.9s2.7-.7 3.6-1.9"/><path d="M9 9.6h.01M15 9.6h.01"/></symbol>
  <symbol id="i-grad" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M2.5 9L12 4.7 21.5 9 12 13.3z"/><path d="M6.2 11v4.3c0 1.7 2.6 3 5.8 3s5.8-1.3 5.8-3V11"/></symbol>
  <symbol id="i-briefcase" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="2.8" y="7" width="18.4" height="13" rx="2.4"/><path d="M9 7V5.2a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2V7"/><path d="M2.8 12.2h18.4"/></symbol>
  <symbol id="i-plane" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M21.5 3.2L2.8 10.6l6.4 2.6 2.5 6.5z"/><path d="M9.2 13.2l4.6-4.4"/></symbol>
  <symbol id="i-wa" viewBox="0 0 24 24"><path fill="currentColor" d="M12.04 2C6.6 2 2.2 6.4 2.2 11.84c0 1.74.46 3.44 1.32 4.94L2 22l5.36-1.4a9.8 9.8 0 0 0 4.68 1.2h.01c5.43 0 9.84-4.4 9.84-9.84 0-2.63-1.02-5.1-2.88-6.96A9.78 9.78 0 0 0 12.04 2zm0 1.8c2.15 0 4.17.84 5.69 2.36a8 8 0 0 1 2.36 5.69c0 4.44-3.6 8.04-8.05 8.04a8.1 8.1 0 0 1-4.1-1.12l-.3-.18-3.05.8.82-2.98-.2-.31a8 8 0 0 1-1.24-4.29c0-4.44 3.62-8.04 8.07-8.04zm-3.6 3.94c-.17 0-.44.06-.67.31-.23.25-.88.86-.88 2.1 0 1.23.9 2.42 1.03 2.59.13.17 1.75 2.8 4.3 3.81 2.12.84 2.55.67 3.01.63.46-.04 1.48-.6 1.69-1.19.21-.58.21-1.08.15-1.19-.06-.1-.23-.17-.48-.29-.25-.13-1.48-.73-1.7-.81-.23-.08-.4-.13-.56.12-.17.25-.65.81-.8.98-.14.17-.29.19-.54.06-.25-.12-1.06-.39-2.02-1.25-.75-.67-1.25-1.5-1.4-1.75-.14-.25-.01-.39.11-.51.11-.11.25-.29.37-.44.13-.15.17-.25.25-.42.09-.17.04-.31-.02-.44-.06-.12-.56-1.35-.77-1.85-.2-.48-.4-.42-.55-.42h-.47z"/></symbol>
  <symbol id="i-ig" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="5.2"/><circle cx="12" cy="12" r="4"/><circle cx="17.3" cy="6.7" r="1.1" fill="currentColor" stroke="none"/></symbol>
  <symbol id="i-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></symbol>
</svg>
"""

FLAG_UK = """<svg viewBox="0 0 60 60" role="img" aria-label="English"><rect width="60" height="60" fill="#012169"/><path d="M0 0l60 60M60 0L0 60" stroke="#ffffff" stroke-width="12"/><path d="M0 0l60 60M60 0L0 60" stroke="#c8102e" stroke-width="5"/><path d="M30 0v60M0 30h60" stroke="#ffffff" stroke-width="18"/><path d="M30 0v60M0 30h60" stroke="#c8102e" stroke-width="10"/></svg>"""
FLAG_ID = """<svg viewBox="0 0 60 60" role="img" aria-label="Indonesian"><rect width="60" height="30" fill="#ce1126"/><rect y="30" width="60" height="30" fill="#ffffff"/></svg>"""
FLAG_RU = """<svg viewBox="0 0 60 60" role="img" aria-label="Russian"><rect width="60" height="20" fill="#ffffff"/><rect y="20" width="60" height="20" fill="#0039a6"/><rect y="40" width="60" height="20" fill="#d52b1e"/></svg>"""


def icon(name, cls=""):
    c = f' class="{cls}"' if cls else ""
    return f'<svg{c} aria-hidden="true"><use href="#i-{name}"/></svg>'


# --------------------------------------------------------------------------- content
C = {}

C["en"] = {
    "lang": "en",
    "meta": {
        "title": "Language Classes — English, Indonesian &amp; Russian | Little Lab Stories (TIAS)",
        "desc": "Personalised online language classes in English, Indonesian and Russian with Ms. Laura and Mr. Rangga. One-to-one, small group and children's classes — flexible schedule, structured curriculum.",
        "og_title": "Language Classes — Learn a New Language. Speak with Confidence.",
        "og_desc": "English, Indonesian and Russian — online, one-to-one, built around your goals. A programme of Little Lab Stories (TIAS).",
    },
    "nav": {"courses": "Courses", "how": "How It Works", "teachers": "Teachers", "faq": "FAQ", "register": "Register"},
    "hero": {
        "kicker": "Personalised language learning",
        "h1": "Learn a New Language.",
        "sub": "Speak with Confidence.",
        "lead": "English, Indonesian and Russian classes — structured, interactive and practical, tailored to your goals. Online, one-to-one, and always at your own pace.",
        "cta1": "Explore our courses",
        "cta2": "Chat on WhatsApp",
        "facts": [("globe", "Online classes"), ("calendar", "Flexible schedule"), ("spark", "Personalised lessons")],
        "badge": "First batch now open",
        "img_alt": "A student smiling during an online language class",
    },
    "courses": {
        "kicker": "Our courses",
        "h2": "Choose Your Language",
        "p": "Three languages, one gentle method: real conversation from the very first session.",
        "meta": "Levels {levels} · 60 minutes · Online",
        "cards": [
            {
                "key": "English", "flag": FLAG_UK, "name": "English", "native": "English · British &amp; American", "img": "london",
                "desc": "Improve your English for everyday communication, study and work.",
                "items": ["Conversation &amp; Speaking", "Vocabulary &amp; Grammar", "Listening", "Reading &amp; Writing", "Pronunciation"],
                "levels": "A1–C1", "cta": "Explore English classes",
            },
            {
                "key": "Indonesian", "flag": FLAG_ID, "name": "Indonesian", "native": "Bahasa Indonesia", "img": "borobudur",
                "desc": "Learn Indonesian for everyday life and speak naturally in Indonesia.",
                "items": ["Everyday Conversation", "Essential Vocabulary", "Grammar &amp; Sentence Patterns", "Formal &amp; Informal Indonesian"],
                "levels": "A1–C1", "cta": "Explore Indonesian classes",
            },
            {
                "key": "Russian", "flag": FLAG_RU, "name": "Russian", "native": "Русский язык", "img": "moscow",
                "desc": "Start Russian from the very basics with a clear and simple approach.",
                "items": ["Cyrillic Alphabet", "Basic Pronunciation", "Everyday Vocabulary", "Simple Conversations"],
                "levels": "A1–B1", "cta": "Explore Russian classes",
            },
        ],
        "note": 'Not sure where you are? <a href="{wa}">Ask for a free 15-minute level check</a> on WhatsApp.',
    },
    "levels": {
        "kicker": "Levels",
        "h2": "Where You Start, Where You Go",
        "p": "Every lesson is mapped to the CEFR scale, so progress is something you can see — not just a feeling.",
        "cefr": [("A1", "Beginner"), ("A2", "Elementary"), ("B1", "Intermediate"), ("B2", "Upper intermediate"), ("C1", "Advanced")],
        "note": "We check your level in a short conversation, then build a plan around it.",
        "cta": "Request a free level check",
    },
    "learn": {
        "kicker": "How you will learn",
        "h2": "A Method That Fits Real Life",
        "p": "No pressure, no endless drills. Just steady progress, one conversation at a time.",
        "items": [
            ("spark", "Personalised learning", "Lessons are built around your goal — work, study, travel, family, or simply confidence."),
            ("chat", "Interactive lessons", "You speak from the first session: role-play, stories and real situations."),
            ("route", "Structured curriculum", "Each level has a clear path, so you always know what comes next."),
            ("book", "Learning materials", "PDF summaries, vocabulary lists and audio practice after every session."),
            ("chart", "Progress &amp; feedback", "Written notes after each class, and a progress review every month."),
        ],
    },
    "formats": {
        "kicker": "Class formats",
        "h2": "Choose How You Learn",
        "p": "Every format is live and online — led by a teacher, never a recorded course.",
        "cards": [
            ("user", "One-to-one", "Full attention on you and your goals. The fastest way to speaking.", "60 minutes · Online · All levels"),
            ("users", "Small group", "Learn with a friend, partner or colleague — share the lesson, share the cost.", "2–4 learners · 60 minutes"),
            ("smile", "Young learners", "Story-based, playful sessions that build a natural feel for the language.", "45 minutes · Ages 6–12"),
        ],
        "fine": "Classes run on Zoom or Google Meet. Materials are included, and session recordings are available on request.",
    },
    "teachers": {
        "kicker": "Your teachers",
        "h2": "Guided by Experienced Teachers",
        "p": "Two teachers, one approach: patient, practical, and genuinely interested in your progress.",
        "list": [
            {
                "name": "Ms. Laura", "role": "English educator", "img": "ms-laura", "alt": "Portrait of Ms. Laura",
                "bio": "Ms. Laura has spent more than a decade teaching in international schools and holds a Master's degree in Communication from the United States. She is known for guiding students and professionals with clarity and confidence — helping them handle academic, professional and cross-cultural conversations with ease.",
                "chips": ["10+ years teaching", "International schools", "MA in Communication (USA)"],
            },
            {
                "name": "Mr. Rangga", "role": "Indonesian teacher · Founder of TIAS", "img": "mr-rangga", "alt": "Portrait of Mr. Rangga (Mr. Birdflute)",
                "bio": "Rangga Firmansyah — known as Mr. Birdflute — is a writer, educator and storyteller, and the author of <em>Everyday Indonesian</em>, a practical guide to daily conversation. He founded Little Lab Stories (TIAS) and teaches Indonesian the way it is actually spoken: warm, informal and full of context.",
                "chips": ["Author of Everyday Indonesian", "Writer, educator &amp; storyteller", "Founder of littlelabstories.com"],
            },
        ],
        "cta": "Ask which class fits you",
    },
    "audience": {
        "kicker": "Who it's for",
        "h2": "Classes for Every Stage of Life",
        "p": "From a child's first English words to a professional presentation — the method adapts, the warmth stays.",
        "items": [
            ("smile", "Young learners", "A strong start through stories, pictures and play."),
            ("grad", "Teenagers &amp; students", "Practical language for school, exams and study abroad."),
            ("briefcase", "Adults &amp; professionals", "Speak clearly in meetings, interviews and everyday work."),
            ("plane", "Expats &amp; travellers", "Find your feet in Indonesia — or wherever the next trip takes you."),
        ],
        "corporate": {
            "title": "Teams &amp; companies",
            "text": "Language training for staff who speak with clients, partners and guests. Tell us the team size and goals — we will propose a programme.",
            "cta": "Ask about corporate classes",
        },
    },
    "steps": {
        "kicker": "How to get started",
        "h2": "Four Simple Steps",
        "p": "From your first message to your first lesson — usually within a week.",
        "items": [
            ("Choose your language", "English, Indonesian or Russian."),
            ("Tell us your goal", "Share your level and what you want to achieve."),
            ("Schedule your lesson", "Pick a day and time that fits your week."),
            ("Start learning", "Begin your personalised programme."),
        ],
    },
    "faq": {
        "kicker": "FAQ",
        "h2": "Questions, Answered",
        "p": "Anything else, just ask on WhatsApp — we answer personally.",
        "items": [
            ("Do I need to know some English to start?", "No. Indonesian and Russian classes start from zero, and English classes are available from beginner level."),
            ("How long is a session, and how many will I need?", "Sessions run 45–60 minutes. Most learners take one or two per week; a full CEFR level usually takes 20–30 sessions, depending on your starting point."),
            ("Can I reschedule?", "Yes. Let us know at least 12 hours before the session and we will move it, free of charge."),
            ("How do I pay?", "Payment is arranged on WhatsApp — bank transfer or e-wallet, per package. Everything is confirmed before your first class."),
            ("Do I get a certificate?", "Yes. A certificate of completion is issued on request after you finish a level."),
            ("Do you teach children?", "Yes. Young learner classes (ages 6–12) use stories, pictures and play, 45 minutes per session."),
            ("What if I live in another time zone?", "Classes are scheduled in WIB (GMT+7). Evening slots work well for Europe, and early mornings for the Americas."),
            ("Can my company book a class?", "Yes. Send us the number of learners and their goals, and we will propose a programme."),
        ],
    },
    "final": {
        "h2": "Ready to Start Learning?",
        "p": "Tell us your language and your goal. We will suggest the right class — and you can start this week.",
        "cta": "Register for a lesson",
        "cta2": "Chat with us first",
        "small": "Replies within office hours, WIB (GMT+7).",
    },
    "footer": {
        "tag": "Taman Imajinasi Anak Semesta",
        "desc": "Little Lab Stories (TIAS) — a creative sanctuary for children's imagination. Language Classes is one of our programmes, alongside our books and creative workshops.",
        "links_title": "Explore",
        "links": [("Home", "index.html"), ("The Books", "index.html#carousel_1fd3"), ("Language Classes", "language-classes.html")],
        "contact_title": "Get in touch",
        "copyright": "© 2026 Little Lab Stories · TIAS. All rights reserved.",
        "back": "Back to Little Lab Stories",
    },
    "wa": {
        "general": wa("Hi Mr. Birdflute, I'd like to ask about the Language Classes at Little Lab Stories (TIAS)."),
        "level": wa("Hi Mr. Birdflute, I'd like to request a free 15-minute level check for my language class."),
        "teacher": wa("Hi Mr. Birdflute, could you help me choose the right language class?"),
        "corporate": wa("Hi Mr. Birdflute, I'd like to ask about corporate language training for my team."),
        "register": wa("Hi Mr. Birdflute, I'd like to register for a language class at Little Lab Stories (TIAS)."),
        "course": "Hi Mr. Birdflute, I'd like to ask about {name} classes at Little Lab Stories (TIAS).",
    },
}

C["id"] = {
    "lang": "id",
    "meta": {
        "title": "Language Classes — English, Indonesian &amp; Russian | Little Lab Stories (TIAS)",
        "desc": "Kelas bahasa online yang personal: English, Indonesian, dan Russian bersama Ms. Laura dan Mr. Rangga. Privat, grup kecil, dan kelas anak — jadwal fleksibel, kurikulum terstruktur.",
        "og_title": "Language Classes — Pelajari Bahasa Baru. Bicara dengan Percaya Diri.",
        "og_desc": "English, Indonesian, dan Russian — online, satu lawan satu, disesuaikan dengan tujuan Anda. Program Little Lab Stories (TIAS).",
    },
    "nav": {"courses": "Kelas", "how": "Cara Belajar", "teachers": "Pengajar", "faq": "FAQ", "register": "Daftar"},
    "hero": {
        "kicker": "Pembelajaran bahasa yang personal",
        "h1": "Pelajari Bahasa Baru.",
        "sub": "Bicara dengan Percaya Diri.",
        "lead": "Kelas English, Indonesian, dan Russian — terstruktur, interaktif, dan praktis, disesuaikan dengan tujuan Anda. Online, satu lawan satu, dengan tempo yang Anda tentukan.",
        "cta1": "Lihat pilihan kelas",
        "cta2": "Chat via WhatsApp",
        "facts": [("globe", "Kelas online"), ("calendar", "Jadwal fleksibel"), ("spark", "Materi personal")],
        "badge": "Batch perdana dibuka",
        "img_alt": "Murid tersenyum mengikuti kelas bahasa online",
    },
    "courses": {
        "kicker": "Pilihan kelas",
        "h2": "Pilih Bahasa Anda",
        "p": "Tiga bahasa, satu metode yang tenang: percakapan nyata sejak sesi pertama.",
        "meta": "Level {levels} · 60 menit · Online",
        "cards": [
            {
                "key": "English", "flag": FLAG_UK, "name": "English", "native": "English · British &amp; American", "img": "london",
                "desc": "Tingkatkan bahasa Inggris untuk komunikasi sehari-hari, studi, dan kerja.",
                "items": ["Percakapan &amp; Berbicara", "Kosakata &amp; Tata Bahasa", "Menyimak", "Membaca &amp; Menulis", "Pelafalan"],
                "levels": "A1–C1", "cta": "Lihat kelas English",
            },
            {
                "key": "Indonesian", "flag": FLAG_ID, "name": "Indonesian", "native": "Bahasa Indonesia", "img": "borobudur",
                "desc": "Belajar bahasa Indonesia untuk kehidupan sehari-hari dan bicara natural di Indonesia.",
                "items": ["Percakapan Sehari-hari", "Kosakata Penting", "Tata Bahasa &amp; Pola Kalimat", "Bahasa Formal &amp; Informal"],
                "levels": "A1–C1", "cta": "Lihat kelas Indonesian",
            },
            {
                "key": "Russian", "flag": FLAG_RU, "name": "Russian", "native": "Русский язык", "img": "moscow",
                "desc": "Mulai bahasa Rusia dari nol dengan pendekatan yang jelas dan sederhana.",
                "items": ["Alfabet Kiril", "Pelafalan Dasar", "Kosakata Sehari-hari", "Percakapan Sederhana"],
                "levels": "A1–B1", "cta": "Lihat kelas Russian",
            },
        ],
        "note": 'Belum tahu level Anda? <a href="{wa}">Minta cek level gratis 15 menit</a> lewat WhatsApp.',
    },
    "levels": {
        "kicker": "Level",
        "h2": "Dari Mana Anda Mulai, Ke Mana Anda Pergi",
        "p": "Setiap sesi dipetakan ke skala CEFR, jadi kemajuan bisa dilihat — bukan cuma dirasakan.",
        "cefr": [("A1", "Pemula"), ("A2", "Dasar"), ("B1", "Menengah"), ("B2", "Menengah atas"), ("C1", "Mahir")],
        "note": "Kami cek level Anda dalam percakapan singkat, lalu menyusun rencana belajarnya.",
        "cta": "Minta cek level gratis",
    },
    "learn": {
        "kicker": "Cara Anda belajar",
        "h2": "Metode yang Masuk ke Kehidupan Nyata",
        "p": "Tanpa tekanan, tanpa latihan gramatika tanpa akhir. Progres tenang, satu percakapan demi satu.",
        "items": [
            ("spark", "Pembelajaran personal", "Sesi dibangun mengikuti tujuan Anda — kerja, studi, perjalanan, keluarga, atau sekadar percaya diri."),
            ("chat", "Kelas interaktif", "Anda bicara sejak sesi pertama: role-play, cerita, dan situasi nyata."),
            ("route", "Kurikulum terstruktur", "Setiap level punya jalur yang jelas, jadi Anda tahu apa yang berikutnya."),
            ("book", "Materi belajar", "Ringkasan PDF, daftar kosakata, dan latihan audio setelah setiap sesi."),
            ("chart", "Progres &amp; umpan balik", "Catatan tertulis setelah kelas dan tinjauan progres setiap bulan."),
        ],
    },
    "formats": {
        "kicker": "Format kelas",
        "h2": "Pilih Cara Belajar Anda",
        "p": "Semua format adalah kelas live bersama pengajar — bukan kursus rekaman.",
        "cards": [
            ("user", "Privat satu lawan satu", "Perhatian penuh untuk Anda dan tujuan Anda. Jalur tercepat untuk bisa bicara.", "60 menit · Online · Semua level"),
            ("users", "Grup kecil", "Belajar bersama teman, pasangan, atau rekan kerja — kelas dan biaya dibagi.", "2–4 murid · 60 menit"),
            ("smile", "Kelas anak", "Sesi berbasis cerita dan permainan yang membangun rasa bahasa secara alami.", "45 menit · Usia 6–12 tahun"),
        ],
        "fine": "Kelas berlangsung lewat Zoom atau Google Meet. Materi sudah termasuk, dan rekaman sesi tersedia atas permintaan.",
    },
    "teachers": {
        "kicker": "Pengajar Anda",
        "h2": "Dipandu Pengajar Berpengalaman",
        "p": "Dua pengajar, satu pendekatan: sabar, praktis, dan sungguh peduli pada kemajuan Anda.",
        "list": [
            {
                "name": "Ms. Laura", "role": "Pengajar Bahasa Inggris", "img": "ms-laura", "alt": "Foto Ms. Laura",
                "bio": "Ms. Laura lebih dari sepuluh tahun mengajar di sekolah internasional dan menyandang gelar Master Komunikasi dari Amerika Serikat. Ia dikenal mampu membimbing murid maupun profesional dengan jelas dan percaya diri — membantu mereka menangani percakapan akademik, profesional, dan lintas budaya.",
                "chips": ["10+ tahun mengajar", "Sekolah internasional", "Master Komunikasi (AS)"],
            },
            {
                "name": "Mr. Rangga", "role": "Pengajar Bahasa Indonesia · Pendiri TIAS", "img": "mr-rangga", "alt": "Foto Mr. Rangga (Mr. Birdflute)",
                "bio": "Rangga Firmansyah — dikenal sebagai Mr. Birdflute — adalah penulis, pendidik, dan pencerita, serta penulis buku <em>Everyday Indonesian</em>, panduan percakapan sehari-hari. Ia mendirikan Little Lab Stories (TIAS) dan mengajarkan bahasa Indonesia seperti yang benar-benar dipakai: hangat, santai, dan kaya konteks.",
                "chips": ["Penulis Everyday Indonesian", "Penulis, pendidik &amp; pencerita", "Pendiri littlelabstories.com"],
            },
        ],
        "cta": "Tanya kelas yang cocok untuk saya",
    },
    "audience": {
        "kicker": "Untuk siapa",
        "h2": "Kelas untuk Setiap Tahap Kehidupan",
        "p": "Dari kata Inggris pertama seorang anak sampai presentasi profesional — metodenya menyesuaikan, kehangatannya tetap.",
        "items": [
            ("smile", "Anak-anak", "Awal yang kuat lewat cerita, gambar, dan permainan."),
            ("grad", "Remaja &amp; pelajar", "Bahasa praktis untuk sekolah, ujian, dan studi ke luar negeri."),
            ("briefcase", "Dewasa &amp; profesional", "Bicara jelas di rapat, wawancara, dan pekerjaan sehari-hari."),
            ("plane", "Expat &amp; pelancong", "Nyaman di Indonesia — dan di mana pun perjalanan berikutnya."),
        ],
        "corporate": {
            "title": "Tim &amp; perusahaan",
            "text": "Pelatihan bahasa untuk staf yang berbicara dengan klien, mitra, dan tamu. Beri tahu jumlah tim dan tujuannya — kami susun programnya.",
            "cta": "Tanya kelas korporat",
        },
    },
    "steps": {
        "kicker": "Cara memulai",
        "h2": "Empat Langkah Sederhana",
        "p": "Dari pesan pertama sampai kelas pertama — biasanya dalam sepekan.",
        "items": [
            ("Pilih bahasa Anda", "English, Indonesian, atau Russian."),
            ("Ceritakan tujuan Anda", "Bagikan level dan target yang ingin dicapai."),
            ("Atur jadwal", "Pilih hari dan jam yang pas dengan minggu Anda."),
            ("Mulai belajar", "Jalani program yang dibuat khusus untuk Anda."),
        ],
    },
    "faq": {
        "kicker": "FAQ",
        "h2": "Pertanyaan yang Sering Ditanyakan",
        "p": "Ada pertanyaan lain? Tanya langsung di WhatsApp — kami jawab pribadi.",
        "items": [
            ("Apakah saya harus bisa bahasa Inggris dulu?", "Tidak. Kelas Indonesian dan Russian dimulai dari nol, dan kelas English tersedia dari level pemula."),
            ("Berapa lama satu sesi dan berapa sesi yang saya butuhkan?", "Sesi 45–60 menit. Umumnya 1–2 sesi per minggu; satu level CEFR biasanya 20–30 sesi, tergantung titik awal Anda."),
            ("Bisa reschedule?", "Bisa. Kabari minimal 12 jam sebelum sesi dan jadwalnya kami pindahkan tanpa biaya."),
            ("Bagaimana pembayarannya?", "Pembayaran diatur lewat WhatsApp — transfer bank atau e-wallet, per paket. Semuanya dikonfirmasi sebelum kelas pertama."),
            ("Apakah ada sertifikat?", "Ada. Sertifikat penyelesaian diberikan atas permintaan setelah Anda menyelesaikan satu level."),
            ("Apakah menerima anak-anak?", "Ya. Kelas anak (6–12 tahun) memakai cerita, gambar, dan permainan, 45 menit per sesi."),
            ("Bagaimana kalau saya di zona waktu lain?", "Jadwal memakai WIB (GMT+7). Slot malam cocok untuk Eropa, dan pagi awal untuk Amerika."),
            ("Bisa untuk perusahaan?", "Bisa. Kirim jumlah peserta dan tujuannya, kami akan menyusun programnya."),
        ],
    },
    "final": {
        "h2": "Siap Mulai Belajar?",
        "p": "Sebutkan bahasa dan tujuan Anda. Kami bantu pilihkan kelasnya — dan Anda bisa mulai minggu ini.",
        "cta": "Daftar kelas",
        "cta2": "Tanya dulu lewat WhatsApp",
        "small": "Balasan di jam kerja, WIB (GMT+7).",
    },
    "footer": {
        "tag": "Taman Imajinasi Anak Semesta",
        "desc": "Little Lab Stories (TIAS) — ruang kreatif untuk imajinasi anak. Language Classes adalah salah satu program kami, bersama buku dan kelas kreatif.",
        "links_title": "Jelajahi",
        "links": [("Beranda", "index.html"), ("Buku", "index.html#carousel_1fd3"), ("Language Classes", "language-classes-id.html")],
        "contact_title": "Hubungi kami",
        "copyright": "© 2026 Little Lab Stories · TIAS. Hak cipta dilindungi.",
        "back": "Kembali ke Little Lab Stories",
    },
    "wa": {
        "general": wa("Halo Mr. Birdflute, saya mau tanya tentang Language Classes di Little Lab Stories (TIAS)."),
        "level": wa("Halo Mr. Birdflute, saya mau minta cek level gratis 15 menit untuk kelas bahasa."),
        "teacher": wa("Halo Mr. Birdflute, boleh bantu saya pilih kelas bahasa yang cocok?"),
        "corporate": wa("Halo Mr. Birdflute, saya mau tanya pelatihan bahasa untuk tim/perusahaan."),
        "register": wa("Halo Mr. Birdflute, saya mau daftar kelas bahasa di Little Lab Stories (TIAS)."),
        "course": "Halo Mr. Birdflute, saya mau tanya kelas {name} di Little Lab Stories (TIAS).",
    },
}

C["ru"] = {
    "lang": "ru",
    "meta": {
        "title": "Курсы языков — английский, индонезийский и русский | Little Lab Stories (TIAS)",
        "desc": "Индивидуальные онлайн-занятия английским, индонезийским и русским с Ms. Laura и Mr. Rangga. Индивидуально, в мини-группе и для детей — гибкий график, структурированная программа.",
        "og_title": "Language Classes — выучите новый язык и говорите уверенно.",
        "og_desc": "Английский, индонезийский и русский — онлайн, один на один, вокруг ваших целей. Программа Little Lab Stories (TIAS).",
    },
    "nav": {"courses": "Курсы", "how": "Как мы учим", "teachers": "Преподаватели", "faq": "Вопросы", "register": "Записаться"},
    "hero": {
        "kicker": "Индивидуальное изучение языков",
        "h1": "Выучите новый язык.",
        "sub": "Говорите уверенно.",
        "lead": "Английский, индонезийский и русский — структурированные, живые и практичные занятия, построенные вокруг ваших целей. Онлайн, один на один и в удобном для вас темпе.",
        "cta1": "Смотреть курсы",
        "cta2": "Написать в WhatsApp",
        "facts": [("globe", "Онлайн-занятия"), ("calendar", "Гибкий график"), ("spark", "Личная программа")],
        "badge": "Первый набор открыт",
        "img_alt": "Ученик на онлайн-занятии по языку",
    },
    "courses": {
        "kicker": "Наши курсы",
        "h2": "Выберите язык",
        "p": "Три языка — один спокойный метод: настоящая речь с первого занятия.",
        "meta": "Уровни {levels} · 60 минут · онлайн",
        "cards": [
            {
                "key": "English", "flag": FLAG_UK, "name": "Английский", "native": "English · British &amp; American", "img": "london",
                "desc": "Улучшите английский для повседневного общения, учёбы и работы.",
                "items": ["Разговорная речь", "Лексика и грамматика", "Аудирование", "Чтение и письмо", "Произношение"],
                "levels": "A1–C1", "cta": "Курс английского",
            },
            {
                "key": "Indonesian", "flag": FLAG_ID, "name": "Индонезийский", "native": "Bahasa Indonesia", "img": "borobudur",
                "desc": "Индонезийский для повседневной жизни — говорите естественно в Индонезии.",
                "items": ["Бытовая речь", "Базовая лексика", "Грамматика и структуры", "Официальный и разговорный язык"],
                "levels": "A1–C1", "cta": "Курс индонезийского",
            },
            {
                "key": "Russian", "flag": FLAG_RU, "name": "Русский", "native": "Русский язык", "img": "moscow",
                "desc": "Начните русский с самых основ — понятно и просто.",
                "items": ["Кириллица", "Базовое произношение", "Повседневная лексика", "Простые диалоги"],
                "levels": "A1–B1", "cta": "Курс русского",
            },
        ],
        "note": 'Не знаете свой уровень? <a href="{wa}">Запросите бесплатную проверку</a> (15 минут) в WhatsApp.',
    },
    "levels": {
        "kicker": "Уровни",
        "h2": "С чего начинаете и куда идёте",
        "p": "Каждое занятие соотнесено со шкалой CEFR — прогресс видно, а не только чувствуется.",
        "cefr": [("A1", "Начальный"), ("A2", "Элементарный"), ("B1", "Средний"), ("B2", "Выше среднего"), ("C1", "Продвинутый")],
        "note": "Определим уровень в коротком разговоре и построим план занятий.",
        "cta": "Бесплатная проверка уровня",
    },
    "learn": {
        "kicker": "Как вы будете учиться",
        "h2": "Метод, который подходит реальной жизни",
        "p": "Без давления и бесконечных упражнений — спокойный прогресс, разговор за разговором.",
        "items": [
            ("spark", "Личная программа", "Занятия строятся вокруг вашей цели: работа, учёба, путешествия, семья."),
            ("chat", "Живые занятия", "Вы говорите с первого занятия: ролевые ситуации, истории, реальные диалоги."),
            ("route", "Структурированный курс", "У каждого уровня понятный маршрут — вы знаете, что будет дальше."),
            ("book", "Учебные материалы", "PDF-конспекты, списки слов и аудиопрактика после каждого занятия."),
            ("chart", "Прогресс и обратная связь", "Заметки после занятия и обзор прогресса раз в месяц."),
        ],
    },
    "formats": {
        "kicker": "Форматы занятий",
        "h2": "Выберите формат",
        "p": "Все форматы — живые онлайн-занятия с преподавателем, а не записанный курс.",
        "cards": [
            ("user", "Индивидуально", "Всё внимание — вам и вашим целям. Самый быстрый путь к речи.", "60 минут · онлайн · любой уровень"),
            ("users", "Мини-группа", "Учитесь с другом, партнёром или коллегой — и делите стоимость.", "2–4 человека · 60 минут"),
            ("smile", "Дети", "Занятия с историями и игрой — естественное чувство языка.", "45 минут · 6–12 лет"),
        ],
        "fine": "Занятия проходят в Zoom или Google Meet. Материалы включены, запись — по запросу.",
    },
    "teachers": {
        "kicker": "Ваши преподаватели",
        "h2": "Опытные преподаватели",
        "p": "Два преподавателя, один подход: внимательно, практично и с настоящим интересом к вашему прогрессу.",
        "list": [
            {
                "name": "Ms. Laura", "role": "Преподаватель английского", "img": "ms-laura", "alt": "Фото Ms. Laura",
                "bio": "Мисс Лаура более десяти лет преподаёт в международных школах и имеет степень магистра коммуникаций (США). Она помогает студентам и специалистам говорить ясно и уверенно — в учёбе, работе и межкультурном общении.",
                "chips": ["10+ лет преподавания", "Международные школы", "Магистр коммуникаций (США)"],
            },
            {
                "name": "Mr. Rangga", "role": "Преподаватель индонезийского · основатель TIAS", "img": "mr-rangga", "alt": "Фото Mr. Rangga (Mr. Birdflute)",
                "bio": "Рангга Фирмансьях (Mr. Birdflute) — писатель, педагог и рассказчик, автор книги <em>Everyday Indonesian</em> о повседневной речи. Он основал Little Lab Stories (TIAS) и учит индонезийскому так, как на нём говорят на самом деле: тепло, просто и с контекстом.",
                "chips": ["Автор Everyday Indonesian", "Писатель, педагог, рассказчик", "Основатель littlelabstories.com"],
            },
        ],
        "cta": "Спросить, какой курс подойдёт",
    },
    "audience": {
        "kicker": "Для кого",
        "h2": "Занятия для любого возраста",
        "p": "От первых английских слов ребёнка до профессиональной презентации — метод подстраивается, тепло остаётся.",
        "items": [
            ("smile", "Дети", "Спокойное начало через истории, картинки и игру."),
            ("grad", "Подростки и студенты", "Практический язык для школы, экзаменов и учёбы за рубежом."),
            ("briefcase", "Взрослые и специалисты", "Говорите уверенно на встречах, интервью и в работе."),
            ("plane", "Экспаты и путешественники", "Освойтесь в Индонезии — и в любой следующей поездке."),
        ],
        "corporate": {
            "title": "Компании и команды",
            "text": "Обучение сотрудников, которые говорят с клиентами, партнёрами и гостями. Расскажите о размере команды и задачах — предложим программу.",
            "cta": "Запросить корпоративный курс",
        },
    },
    "steps": {
        "kicker": "Как начать",
        "h2": "Четыре простых шага",
        "p": "От первого сообщения до первого занятия — обычно в течение недели.",
        "items": [
            ("Выберите язык", "Английский, индонезийский или русский."),
            ("Расскажите о цели", "Ваш уровень и чего вы хотите достичь."),
            ("Выберите время", "День и время, удобные для вас."),
            ("Начните учиться", "Стартуйте по личной программе."),
        ],
    },
    "faq": {
        "kicker": "Вопросы",
        "h2": "Частые вопросы",
        "p": "Есть другой вопрос? Напишите в WhatsApp — отвечаем лично.",
        "items": [
            ("Нужно ли знать английский, чтобы начать?", "Нет. Индонезийский и русский начинаются с нуля, английский — с любого уровня."),
            ("Сколько длится занятие и сколько их нужно?", "Занятие 45–60 минут. Обычно 1–2 в неделю; полный уровень CEFR — примерно 20–30 занятий, в зависимости от старта."),
            ("Можно перенести занятие?", "Да, бесплатно, если предупредить минимум за 12 часов."),
            ("Как происходит оплата?", "Оплата обсуждается в WhatsApp: перевод на банковский счёт или электронный кошелёк, по пакету. Всё подтверждаем до первого занятия."),
            ("Выдаёте сертификат?", "Да, по запросу после завершения уровня."),
            ("Вы работаете с детьми?", "Да. Занятия для детей 6–12 лет: истории, картинки и игра, 45 минут."),
            ("А если я в другом часовом поясе?", "Занятия по времени WIB (GMT+7). Вечерние часы подходят для Европы, раннее утро — для Америки."),
            ("Может ли компания заказать занятия?", "Да. Пришлите число сотрудников и цели — предложим программу."),
        ],
    },
    "final": {
        "h2": "Готовы начать?",
        "p": "Напишите, какой язык и какая цель. Подскажем подходящий курс — и вы сможете начать на этой неделе.",
        "cta": "Записаться на занятие",
        "cta2": "Сначала написать нам",
        "small": "Отвечаем в рабочее время, WIB (GMT+7).",
    },
    "footer": {
        "tag": "Taman Imajinasi Anak Semesta",
        "desc": "Little Lab Stories (TIAS) — творческое пространство для детского воображения. Language Classes — одна из наших программ, вместе с книгами и творческими мастерскими.",
        "links_title": "Разделы",
        "links": [("Главная", "index.html"), ("Книги", "index.html#carousel_1fd3"), ("Language Classes", "language-classes-ru.html")],
        "contact_title": "Связаться",
        "copyright": "© 2026 Little Lab Stories · TIAS. Все права защищены.",
        "back": "Вернуться на Little Lab Stories",
    },
    "wa": {
        "general": wa("Здравствуйте, Mr. Birdflute! Хочу узнать о Language Classes в Little Lab Stories (TIAS)."),
        "level": wa("Здравствуйте, Mr. Birdflute! Хочу бесплатную 15-минутную проверку уровня."),
        "teacher": wa("Здравствуйте, Mr. Birdflute! Помогите, пожалуйста, выбрать подходящий курс."),
        "corporate": wa("Здравствуйте, Mr. Birdflute! Хочу узнать о корпоративном обучении для команды."),
        "register": wa("Здравствуйте, Mr. Birdflute! Хочу записаться на занятие в Little Lab Stories (TIAS)."),
        "course": "Здравствуйте, Mr. Birdflute! Хочу узнать о курсе «{name}» в Little Lab Stories (TIAS).",
    },
}


# --------------------------------------------------------------------------- render
def render(code):
    d = C[code]
    L = d["lang"]
    nav = d["nav"]
    hero = d["hero"]
    H = []

    reg = d["wa"]["register"]
    wa_general = d["wa"]["general"]
    page = PAGES[code]

    H.append(f"""<!DOCTYPE html>
<html lang="{L}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{d['meta']['title']}</title>
<meta name="description" content="{d['meta']['desc']}">
<link rel="canonical" href="{SITE}/{page}">
<link rel="alternate" hreflang="en" href="{SITE}/{PAGES['en']}">
<link rel="alternate" hreflang="id" href="{SITE}/{PAGES['id']}">
<link rel="alternate" hreflang="ru" href="{SITE}/{PAGES['ru']}">
<link rel="alternate" hreflang="x-default" href="{SITE}/{PAGES['en']}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Little Lab Stories · TIAS">
<meta property="og:title" content="{d['meta']['og_title']}">
<meta property="og:description" content="{d['meta']['og_desc']}">
<meta property="og:url" content="{SITE}/{page}">
<meta property="og:image" content="{SITE}/images/lang/hero-learning.jpg">
<meta property="og:image:alt" content="{hero['img_alt']}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{d['meta']['og_title']}">
<meta name="twitter:description" content="{d['meta']['og_desc']}">
<meta name="twitter:image" content="{SITE}/images/lang/hero-learning.jpg">
<meta name="theme-color" content="#16293f">
<link rel="icon" href="images/TIASlogonew.png">
<link rel="apple-touch-icon" href="images/lang/logo-tias-256.webp">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;1,500&family=Inter:wght@400;500;600&display=swap">
<link rel="stylesheet" href="language-classes.css">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": "EducationalOrganization",
      "@id": "{SITE}/#organization",
      "name": "Little Lab Stories (TIAS)",
      "alternateName": "Taman Imajinasi Anak Semesta",
      "url": "{SITE}/",
      "logo": "{SITE}/images/TIASlogonew.png",
      "sameAs": ["https://www.instagram.com/mr.birdflute/"]
    }},
    {{
      "@type": "WebPage",
      "@id": "{SITE}/{page}",
      "url": "{SITE}/{page}",
      "name": "{d['meta']['og_title']}",
      "inLanguage": "{L}",
      "isPartOf": {{ "@id": "{SITE}/#organization" }}
    }},
    {{
      "@type": "Course",
      "name": "English classes",
      "description": "Online one-to-one English classes: conversation, vocabulary, listening, reading and writing, pronunciation.",
      "inLanguage": "en",
      "provider": {{ "@id": "{SITE}/#organization" }},
      "hasCourseInstance": {{ "@type": "CourseInstance", "courseMode": "Online", "courseWorkload": "PT1H" }}
    }},
    {{
      "@type": "Course",
      "name": "Indonesian classes",
      "description": "Online one-to-one Indonesian classes for everyday conversation, from beginner to advanced.",
      "inLanguage": "id",
      "provider": {{ "@id": "{SITE}/#organization" }},
      "hasCourseInstance": {{ "@type": "CourseInstance", "courseMode": "Online", "courseWorkload": "PT1H" }}
    }},
    {{
      "@type": "Course",
      "name": "Russian classes",
      "description": "Online Russian classes from the very basics: Cyrillic alphabet, pronunciation, everyday vocabulary and simple conversations.",
      "inLanguage": "ru",
      "provider": {{ "@id": "{SITE}/#organization" }},
      "hasCourseInstance": {{ "@type": "CourseInstance", "courseMode": "Online", "courseWorkload": "PT1H" }}
    }}
  ]
}}
</script>
</head>
<body>
<a class="skip-link" href="#main">{nav['courses']}</a>
""")

    # header
    H.append(f"""<header class="site-header">
  <div class="wrap site-header__inner">
    <a class="brand" href="index.html" aria-label="Little Lab Stories — home">
      <span class="brand__logo"><img src="images/lang/logo-tias-128.webp" width="128" height="128" alt="TIAS logo"></span>
      <span class="brand__text">
        <span class="brand__name">Little Lab Stories</span>
        <span class="brand__sub">Language Classes</span>
      </span>
    </a>
    <nav class="nav" aria-label="Sections">
      <a href="#courses">{nav['courses']}</a>
      <a href="#how">{nav['how']}</a>
      <a href="#teachers">{nav['teachers']}</a>
      <a href="#faq">{nav['faq']}</a>
    </nav>
    <div class="header__actions">
      <div class="lang-switch" aria-label="Language">
        {lang_links(code)}
      </div>
      <a class="btn btn--navy btn--sm" href="{reg}" target="_blank" rel="noopener">{nav['register']}</a>
    </div>
  </div>
</header>
<main id="main">
""")

    # hero
    facts = "".join(
        f'<li>{icon(i)}<span>{t}</span></li>' for i, t in hero["facts"]
    )
    H.append(f"""<section class="hero">
  <div class="wrap hero__grid">
    <div class="hero__text">
      <p class="kicker">{hero['kicker']}</p>
      <h1>{hero['h1']}</h1>
      <p class="hero__sub">{hero['sub']}</p>
      <p class="hero__lead">{hero['lead']}</p>
      <div class="hero__cta">
        <a class="btn btn--gold" href="#courses">{hero['cta1']} {icon('arrow')}</a>
        <a class="btn btn--ghost" href="{wa_general}" target="_blank" rel="noopener">{icon('wa')} {hero['cta2']}</a>
      </div>
      <ul class="hero__facts">{facts}</ul>
    </div>
    <div class="hero__media">
      <img src="images/lang/hero-learning.webp" width="988" height="798" alt="{hero['img_alt']}" fetchpriority="high" decoding="async">
      <span class="hero__badge"><span class="dot" aria-hidden="true"></span>{hero['badge']}</span>
    </div>
  </div>
</section>
""")

    # courses
    cards = []
    for c in d["courses"]["cards"]:
        items = "".join(f"<li>{i}</li>" for i in c["items"])
        msg = wa(d["wa"]["course"].format(name=c["key"]))
        cards.append(f"""      <article class="lang-card" data-reveal>
        <div class="lang-card__media">
          <img src="images/lang/{c['img']}.webp" width="717" height="380" alt="" loading="lazy" decoding="async">
          <span class="flag">{c['flag']}</span>
        </div>
        <div class="lang-card__body">
          <p class="lang-card__eyebrow">{c['native']}</p>
          <h3>{c['name']}</h3>
          <p class="lang-card__desc">{c['desc']}</p>
          <ul class="ticks">{items}</ul>
          <p class="lang-card__meta">{d['courses']['meta'].format(levels=c['levels'])}</p>
          <a class="lang-card__cta" href="{msg}" target="_blank" rel="noopener">{c['cta']} {icon('arrow')}</a>
        </div>
      </article>""")

    H.append(f"""<section class="section" id="courses">
  <div class="wrap">
    <div class="sec-head" data-reveal>
      <p class="kicker">{d['courses']['kicker']}</p>
      <h2>{d['courses']['h2']}</h2>
      <p>{d['courses']['p']}</p>
      <span class="rule" aria-hidden="true"></span>
    </div>
    <div class="lang-grid">
{chr(10).join(cards)}
    </div>
    <p class="note-line" data-reveal>{d['courses']['note'].format(wa=d['wa']['level'])}</p>
  </div>
</section>
""")

    # levels
    cefr = "".join(f"<li><b>{a}</b><span>{b}</span></li>" for a, b in d["levels"]["cefr"])
    H.append(f"""<section class="section section--cream section--tight" id="levels">
  <div class="wrap levels">
    <div data-reveal>
      <p class="kicker">{d['levels']['kicker']}</p>
      <h2 class="levels__title">{d['levels']['h2']}</h2>
      <p class="levels__p">{d['levels']['p']}</p>
      <p class="levels__note">{d['levels']['note']}</p>
      <div class="levels__cta"><a class="btn btn--navy btn--sm" href="{d['wa']['level']}" target="_blank" rel="noopener">{d['levels']['cta']} {icon('arrow')}</a></div>
    </div>
    <ul class="cefr" data-reveal>{cefr}</ul>
  </div>
</section>
""")

    # learn
    learn = "".join(f"""      <article class="learn-item" data-reveal>
        <span class="learn-item__icon">{icon(i[0])}</span>
        <h3>{i[1]}</h3>
        <p>{i[2]}</p>
      </article>""" for i in d["learn"]["items"])
    H.append(f"""<section class="section" id="how">
  <div class="wrap">
    <div class="sec-head" data-reveal>
      <p class="kicker">{d['learn']['kicker']}</p>
      <h2>{d['learn']['h2']}</h2>
      <p>{d['learn']['p']}</p>
    </div>
    <div class="learn-grid">
{learn}
    </div>
  </div>
</section>
""")

    # formats
    fmts = "".join(f"""      <article class="format-card" data-reveal>
        <span class="format-card__icon">{icon(i[0])}</span>
        <h3>{i[1]}</h3>
        <p>{i[2]}</p>
        <p class="format-card__meta">{i[3]}</p>
      </article>""" for i in d["formats"]["cards"])
    H.append(f"""<section class="section section--cream" id="formats">
  <div class="wrap">
    <div class="sec-head" data-reveal>
      <p class="kicker">{d['formats']['kicker']}</p>
      <h2>{d['formats']['h2']}</h2>
      <p>{d['formats']['p']}</p>
    </div>
    <div class="format-grid">
{fmts}
    </div>
    <p class="fineprint" data-reveal>{d['formats']['fine']}</p>
  </div>
</section>
""")

    # teachers
    tch = []
    for t in d["teachers"]["list"]:
        chips = "".join(f"<li>{x}</li>" for x in t["chips"])
        tch.append(f"""      <article class="teacher" data-reveal>
        <div class="teacher__photo">
          <img src="images/lang/{t['img']}.webp" width="700" height="875" alt="{t['alt']}" loading="lazy" decoding="async">
        </div>
        <div class="teacher__body">
          <h3>{t['name']}</h3>
          <p class="teacher__role">{t['role']}</p>
          <p>{t['bio']}</p>
          <ul class="chips">{chips}</ul>
        </div>
      </article>""")
    H.append(f"""<section class="section" id="teachers">
  <div class="wrap">
    <div class="sec-head" data-reveal>
      <p class="kicker">{d['teachers']['kicker']}</p>
      <h2>{d['teachers']['h2']}</h2>
      <p>{d['teachers']['p']}</p>
    </div>
    <div class="teacher-grid">
{chr(10).join(tch)}
    </div>
    <div class="teachers__cta" data-reveal>
      <a class="btn btn--ghost" href="{d['wa']['teacher']}" target="_blank" rel="noopener">{icon('wa')} {d['teachers']['cta']}</a>
    </div>
  </div>
</section>
""")

    # audience
    aud = "".join(f"""      <li data-reveal>
        <span class="audience__icon">{icon(i[0])}</span>
        <div>
          <h3>{i[1]}</h3>
          <p>{i[2]}</p>
        </div>
      </li>""" for i in d["audience"]["items"])
    corp = d["audience"]["corporate"]
    H.append(f"""<section class="section section--cream" id="for-who">
  <div class="wrap">
    <div class="sec-head" data-reveal>
      <p class="kicker">{d['audience']['kicker']}</p>
      <h2>{d['audience']['h2']}</h2>
      <p>{d['audience']['p']}</p>
    </div>
    <ul class="audience">
{aud}
    </ul>
    <div class="corporate" data-reveal>
      <div>
        <h3>{corp['title']}</h3>
        <p>{corp['text']}</p>
      </div>
      <a class="btn btn--gold btn--sm" href="{d['wa']['corporate']}" target="_blank" rel="noopener">{corp['cta']} {icon('arrow')}</a>
    </div>
  </div>
</section>
""")

    # steps
    steps = "".join(f"""      <li class="step" data-reveal>
        <span class="step__num">{n}</span>
        <h3>{t}</h3>
        <p>{p}</p>
      </li>""" for n, (t, p) in enumerate(d["steps"]["items"], start=1))
    H.append(f"""<section class="section" id="start">
  <div class="wrap">
    <div class="sec-head" data-reveal>
      <p class="kicker">{d['steps']['kicker']}</p>
      <h2>{d['steps']['h2']}</h2>
      <p>{d['steps']['p']}</p>
    </div>
    <ol class="steps" style="list-style:none">
{steps}
    </ol>
  </div>
</section>
""")

    # faq
    faqs = "".join(f"""      <details data-reveal>
        <summary>{q}</summary>
        <p>{a}</p>
      </details>""" for q, a in d["faq"]["items"])
    H.append(f"""<section class="section section--cream" id="faq">
  <div class="wrap">
    <div class="sec-head" data-reveal>
      <p class="kicker">{d['faq']['kicker']}</p>
      <h2>{d['faq']['h2']}</h2>
      <p>{d['faq']['p']}</p>
    </div>
    <div class="faq">
{faqs}
    </div>
  </div>
</section>
""")

    # final
    fin = d["final"]
    H.append(f"""<section class="final">
  <div class="wrap">
    <div class="final__panel" data-reveal>
      <h2>{fin['h2']}</h2>
      <p>{fin['p']}</p>
      <div class="final__cta">
        <a class="btn btn--gold" href="{reg}" target="_blank" rel="noopener">{icon('wa')} {fin['cta']}</a>
        <a class="btn btn--ghost" href="{wa_general}" target="_blank" rel="noopener">{fin['cta2']}</a>
      </div>
      <p class="final__small">{fin['small']}</p>
    </div>
  </div>
</section>
</main>
""")

    # footer
    f = d["footer"]
    flinks = "".join(f'<li><a href="{u}">{t}</a></li>' for t, u in f["links"])
    H.append(f"""<footer class="site-footer">
  <div class="wrap">
    <div class="footer__grid">
      <div class="footer__brand-col">
        <div class="footer__brand">
          <span class="brand__logo"><img src="images/lang/logo-tias-128.webp" width="128" height="128" alt="TIAS logo"></span>
          <span>
            <span class="footer__name">Little Lab Stories</span>
            <span class="footer__tag">{f['tag']}</span>
          </span>
        </div>
        <p class="footer__desc">{f['desc']}</p>
      </div>
      <div>
        <p class="footer__title">{f['links_title']}</p>
        <ul class="footer__links">{flinks}</ul>
      </div>
      <div>
        <p class="footer__title">{f['contact_title']}</p>
        <ul class="footer__links">
          <li><a href="{wa_general}" target="_blank" rel="noopener">WhatsApp &nbsp;+62 859-2116-2228</a></li>
          <li><a href="https://www.instagram.com/mr.birdflute/" target="_blank" rel="noopener">Instagram &nbsp;@mr.birdflute</a></li>
          <li><a href="{page}#faq">{nav['faq']}</a></li>
        </ul>
      </div>
    </div>
    <div class="footer__bottom">
      <span>{f['copyright']}</span>
      <a href="index.html">{f['back']} →</a>
    </div>
  </div>
</footer>

<div class="mobile-bar">
  <a class="btn btn--ghost btn--sm" href="{wa_general}" target="_blank" rel="noopener">{icon('wa')} WhatsApp</a>
  <a class="btn btn--gold btn--sm" href="{reg}" target="_blank" rel="noopener">{nav['register']}</a>
</div>

{SPRITE}
<noscript><style>.mobile-bar{{transform:none}}</style></noscript>
<script>
(function () {{
  var els = document.querySelectorAll('[data-reveal]');
  if ('IntersectionObserver' in window && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {{
    var io = new IntersectionObserver(function (entries) {{
      entries.forEach(function (e) {{
        if (e.isIntersecting) {{ e.target.classList.add('reveal', 'is-visible'); io.unobserve(e.target); }}
      }});
    }}, {{ rootMargin: '0px 0px -8% 0px', threshold: 0.08 }});
    els.forEach(function (el) {{ el.classList.add('reveal'); io.observe(el); }});
  }}

  var bar = document.querySelector('.mobile-bar');
  if (bar) {{
    var toggle = function () {{
      bar.classList.toggle('is-shown', window.scrollY > 260);
    }};
    toggle();
    window.addEventListener('scroll', toggle, {{ passive: true }});
  }}
}})();
</script>
</body>
</html>
""")

    return "\n".join(H)


def lang_links(current):
    out = []
    for code in ("en", "id", "ru"):
        label = code.upper()
        if code == current:
            out.append(f'<span class="is-active" aria-current="page">{label}</span>')
        else:
            out.append(f'<a href="{PAGES[code]}" hreflang="{code}" lang="{code}">{label}</a>')
    return "".join(out)


def main():
    for code, filename in PAGES.items():
        html = render(code)
        path = os.path.join(OUT_DIR, filename)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(html)
        print(f"{path}  {len(html)/1024:.1f} KB")


if __name__ == "__main__":
    main()
