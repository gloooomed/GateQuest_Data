# 🧠 GateQuest_Data

This repository contains structured, cleaned, and collaboratively verified GATE CSE questions in JSON format. These questions are scraped from [GateOverflow](https://gateoverflow.in/) and processed to build an open, community-maintained dataset useful for GATE preparation platforms, research, and practice apps.

> 💡 This dataset is being manually cleaned by contributors to ensure consistent structure, accurate tagging, correct answers, and clear formatting.

> Check the [CONTRIBUTION](CONTRIBUTING.md) Guideline and [PROGRESS](PROGRESS.md) to check for unassigned chunks.
---

## 📁 Structure

All JSON files are split into smaller chunks of 50 questions each, organized by subject and year.


split\_chunks/
├── subject\_chunk\_1.json
├── subject\_chunk\_2.json
├── ...


Each JSON object follows a strict schema:

```json
{
  "id": "dynamic",
  "year": 2024,
  "questionNumber": 35,
  "subject": "subject-name",
  "topic": "pick it from the tags",
  "questionType": "multiple-choice",
  "question": "Question text here...",
  "options": ["A", "B", "C", "D"],
  "correctAnswer": ["A"] or numerical-answer,
  "answerText": null,
  "difficulty": "Easy=easy/Medium=Normal/Hard",
  "marks": 1/2,
  "tags": ["/algorithms", "/graph-search"],
  "source": "gateoverflow",
  "sourceURL": "https://gateoverflow.in/...",
  "addedBy": "GO Scraper",
  "verified": true,
  "explanation": "https://gateoverflow.in/...",
  "metadata": {
    "set": "CS",
    "paperType": "official",
    "language": "English"
  }
}
````

---

## 🚧 Work in Progress

* The data is still being cleaned.
* Many questions have issues like:

  * Mixed question and options
  * Incorrect or missing answers
  * Improper tagging or formatting

We are fixing these **manually**. Help is appreciated! 🙏

---

## 🧑‍💻 Contributing

### ✅ How to Contribute

1. **Check open issues or discussions** to see which chunk is being worked on.
2. **Claim a chunk** by commenting on an issue or announcing it in the group.
3. Edit only the assigned chunk (located in `split_chunks/`)
4. Once done, commit your changes and open a **Pull Request**.

### 📦 Pull Request Format

```text
Title: Fixed algorithms_chunk_2.json - cleaned 50 questions

Description:
- Fixed option separation for all 50 questions
- Normalized tags
- Updated year using tags
- Verified structure and LaTeX formatting
- Answers from the GateOverflow site

Contributor: @yourusername
```

---

## 🛠 Local Setup

```bash
# Clone the repo
git clone https://github.com/Razen04/GateQuest_Data
cd GateQuest_Data
```

---

## 📢 Goals

* Make a free, accurate, verified dataset of GATE CSE questions
* Enable GATE aspirants and devs to build open tools around this
* Encourage contributions and community-driven development

---

## ⚖️ License

This project is released under the **MIT License**. You are free to use, modify, and distribute with attribution.

---

## 🤝 Acknowledgements

* Thanks to [GateOverflow](https://gateoverflow.in/) for the original question data.
* Inspired by the need for better open educational tools for GATE aspirants.

---

> 🗣️ Want to help? Raise an issue, grab a chunk, and start fixing! Every contribution counts!
