# 🎧 AudioFrontier

AudioFrontierは、**まだ存在しない音楽**を探求する、予測的な音楽推薦エンジンです。

既存の楽曲を推薦するのではなく、ユーザーのテキスト入力に基づいて**斬新な音楽の設計図**を生成します。

---

## 🚀 Features

- Text → semantic embedding (MiniLM)
- Audio feature extraction (Essentia)
- Hybrid vector search (FAISS)
- Novelty scoring (distance + density + tags)
- Blueprint generation for unheard music

---

## 🧠 Architecture

User Input → Embedding → Feature Fusion → FAISS  
→ Novelty Engine → Blueprint Generator

---

## 📦 Tech Stack

- FastAPI
- FAISS
- SentenceTransformers
- Essentia
- Docker / Devcontainer

---

## 🐳 Run with Docker

```bash
docker-compose up --build
