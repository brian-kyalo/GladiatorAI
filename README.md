# 🥊 GladiatorAI

> An AI-powered UFC fight prediction platform built from the ground up using data science, machine learning, FastAPI, and Flutter.

---

## Overview

Predicting the outcome of a mixed martial arts fight is a challenging problem. Every matchup is influenced by a combination of striking ability, grappling, age, experience, reach, fighting style, recent performance, and many other factors.

Most public prediction models focus only on training an algorithm, often overlooking the most important part of any machine learning project:

- How should the data be structured?
- Which features actually matter?
- How do we avoid data leakage?
- How can we represent a fighter's progression over time?

GladiatorAI is being built to answer those questions before training a single model.

The goal is to build an end-to-end machine learning system capable of generating meaningful pre-fight predictions using carefully engineered historical UFC data.

---

# Project Goals

- Design a high-quality machine learning dataset for UFC fights.
- Build an automated data collection pipeline.
- Engineer meaningful predictive features.
- Train and evaluate multiple machine learning models.
- Expose predictions through a FastAPI backend.
- Deliver predictions through a cross-platform Flutter application.

---

# Tech Stack

## Machine Learning

- Python
- Pandas
- NumPy
- Scikit-learn
- Jupyter Notebook

## Backend

- FastAPI
- Pydantic
- Uvicorn

## Mobile

- Flutter
- Dart

## Development

- Git
- GitHub Projects
- GitHub Issues
- VS Code

---

# Repository Structure

```
GladiatorAI/

├── backend/
│   ├── .venv/
│   └── requirements.txt
│
├── flutter_app/
│
├── notebooks/
│   └── 00_Playground.ipynb
│
├── datasets/
│
├── models/
│
├── docs/
│
├── README.md
└── .gitignore
```

---

# Development Roadmap

## ✅ Phase 1 — Repository Engineering

Project foundation completed.

- Git repository
- GitHub workflow
- Python environment
- Flutter environment
- Jupyter notebooks
- Project structure
- Version control

---

## 🚧 Phase 2 — Dataset Architecture

Current milestone.

Focus areas:

- Define prediction target
- Design dataset schema
- Identify data sources
- Prevent data leakage
- Plan feature engineering
- Produce data dictionary

---

## ⏳ Phase 3 — Data Collection

- UFC data acquisition
- Historical fight records
- Fighter statistics
- Data validation
- Automated collection pipeline

---

## ⏳ Phase 4 — Exploratory Data Analysis

- Dataset exploration
- Missing value analysis
- Feature distributions
- Correlation analysis
- Initial insights

---

## ⏳ Phase 5 — Feature Engineering

- Fighter aggregates
- Rolling statistics
- Time-based features
- Style matchups
- Recent form metrics

---

## ⏳ Phase 6 — Machine Learning

- Baseline model
- Model comparison
- Hyperparameter tuning
- Performance evaluation
- Model selection

---

## ⏳ Phase 7 — Backend API

- FastAPI
- Prediction endpoint
- Documentation
- Model serving

---

## ⏳ Phase 8 — Flutter Application

- User interface
- Fighter search
- Fight predictions
- Statistics dashboard

---

## ⏳ Phase 9 — Production Release

- Deployment
- Monitoring
- Documentation
- Version 1.0

---

# Current Status

**Current Phase**

Repository Engineering ✅

The project is now transitioning into dataset architecture, where the machine learning problem will be designed before any model training begins.

---

# Engineering Philosophy

This project follows a **data-first** approach.

Instead of selecting an algorithm first, GladiatorAI focuses on designing a high-quality dataset before any machine learning model is trained.

The development workflow is:

```
Problem Definition
        ↓
Dataset Design
        ↓
Data Collection
        ↓
Feature Engineering
        ↓
Model Training
        ↓
Evaluation
        ↓
API
        ↓
Flutter Application
```

Every design decision is documented to ensure the resulting models learn from meaningful, real-world information rather than accidental correlations or leaked data.

---

# Getting Started

Clone the repository.

```bash
git clone https://github.com/brian-kyalo/GladiatorAI.git
```

Navigate into the project.

```bash
cd GladiatorAI
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate the environment.

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies.

```bash
pip install -r backend/requirements.txt
```

Launch Jupyter.

```bash
jupyter notebook
```

---

# Project Management

Development follows a structured GitHub workflow.

- GitHub Issues
- Milestones
- Feature Branches
- Pull Requests
- Conventional Commits

Every feature is linked to an issue before development begins.

---

# Future Work

- Automated UFC data pipeline
- Advanced feature engineering
- Ensemble machine learning models
- Explainable AI predictions
- Fighter comparison dashboard
- Mobile application deployment

---

# License

MIT License

---

> *"Great machine learning models are built on great datasets—not just great algorithms."*