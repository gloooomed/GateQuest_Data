# 🛠️ Contributing to GateQuest_Data

Thanks for considering contributing to **GateQuest_Data**! 🎉  
This guide will help you get started with fixing question data, maintaining consistency, and submitting pull requests.

---

## 🚀 Getting Started

### 1. Fork the Repo

- Go to [GateQuest_Data](https://github.com/Razen04/GateQuest_Data)
- Click the **Fork** button in the top right
- Clone your fork locally:

```bash
git clone https://github.com/Razen04/GateQuest_Data
cd GateQuest_Data
```

---

## 📁 Folder Structure

All questions are inside the `split_chunks/` folder and divided into files of 50 questions each.

> **Example**: `algorithms_chunk_1.json`

---

## 📌 Rules While Editing

### ✅ What You Can Fix

* Use the [preview.html](preview.html) to check the latex formatting locally on your own device.
* Take help from the original question link from the sourceUrl value of that particular object in the json.
* Separate `question` and `options` (fix merged/malformed questions)
* Ensure options are an array of strings in case of MCQ and empty in case of numerical based question
* Extract `year` from tags (e.g. `/tag/gatecse2023-set1` → `year: 2023`)
* Format LaTeX properly for math-heavy questions
* Fill `correctAnswer` from the GateOverflow website
* Add missing or corrected tags (like `/dynamic-programming`, `/greedy`)
* Assign `difficulty` to be `Easy` for 1/2 mark questions and `Medium/hard` for marks greater than 2
* Add marks value as integer by taking a look at the tags in the object
* If any object is there with empty question it can be removed but **mention it in your Pull Request**

### ❌ What Not to Do

* Don’t change unrelated questions you didn't work on
* Don’t edit the `id` field
* Don’t remove source or explanation links

---

### 🧪 Validating Your Chunk Locally
Before making a pull request, validate that your chunk follows the required schema.

Use the command below by passing your file path:

```bash
python .github/scripts/validate_json.py Algorithms/split_chunks/algorithms_chunk_3.json
Replace the path with the file you’re assigned.
```

❗ Do not run the script on the entire directory unless you're a maintainer. It may show irrelevant errors for chunks still under progress.

---

## 🧑‍💻 Claiming a Chunk

To avoid conflicts:

1. Open an issue or discussion titled like:
   `📌 I am working on: algorithms_chunk_2.json`
2. Wait for approval/acknowledgment
3. Start editing once it’s assigned

> This avoids multiple people editing the same file.

---

## 🧾 Submitting Your Pull Request

Once you're done:

1. Commit your changes with a descriptive message:

   ```bash
   git add split_chunks/algorithms_2024_chunk_2.json
   git commit -m "Fixed algorithms_chunk_2.json: separated options and updated year"
   git push
   ```

2. Open a **Pull Request** on GitHub

3. In the PR description, include:

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

## 🙌 Getting Help

If you're stuck:

* Create an issue describing your problem
* Ping [Razen04](https://github.com/Razen04) in the PR/issue comments

---

## 🎯 Our Goal

Build a **100% consistent, clean, verified** question bank of GATE CSE questions for use in apps, websites, and prep tools. Open, community-owned, and useful for all.

---

Thank you again for contributing! 🚀

– GateQuest Team