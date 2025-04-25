# Local Cultural Events Promotion System (Python + Flask)

## Project Description

This repository hosts the source code for a web application built with Python and the Flask framework. The purpose of the system is to register, manage, and promote local cultural events. It is designed for small towns and cultural institutions (such as community centers and cultural foundations) that need a simple, user-friendly platform to showcase fairs, concerts, exhibitions, and other cultural activities.

---

## Theme and Rationale

### Theme

A digital platform for promoting cultural events in small cities.

### Rationale

In many small communities, the lack of accessible digital tools for event promotion limits the reach and visibility of cultural activities that could strengthen local identity. By digitizing the process of event registration and promotion, we aim to:

- Provide the community with up-to-date information on cultural and leisure activities.
- Increase public engagement in local initiatives.
- Connect cultural organizers with sponsors, partners, and attendees.

### Alignment with Sustainable Development Goals (SDGs)

- **SDG 11.4 – Strengthen efforts to protect and safeguard the world’s cultural and natural heritage**  
  This system contributes to the preservation and appreciation of intangible cultural heritage by documenting, publicizing, and archiving events that reflect local traditions and practices.

- **SDG 4.7 – Ensure that all learners acquire the knowledge and skills needed to promote sustainable development, including through education for sustainable lifestyles, human rights, gender equality, promotion of a culture of peace and non-violence, global citizenship, and appreciation of cultural diversity and of culture’s contribution to sustainable development**  
  The platform provides an educational space, allowing schools, universities, and the general public to discover and participate in cultural activities, fostering learning and respect for cultural diversity.

### Soft Skills Developed

Throughout the development of this project, we practiced and improved the following competencies:

- **Problem Solving:** gathering requirements, debugging errors, and optimizing user workflows.
- **Communication and Teamwork:** writing clear documentation, participating in code reviews, and integrating feedback.
- **Time Management and Prioritization:** planning feature milestones, deadlines for deliverables, and testing phases.

---

## Key Features

- Event registration (title, date, location, description, image)
- Listing and searching events by date or category
- Editing and deleting events
- Administrative dashboard for quick management
- Public-facing page for general audience access

---

## Technologies Used

- **Python 3.x**
- **Flask**
- **Jinja2** (templating engine)
- **SQLite** (lightweight database)
- **Git/GitHub** (version control and code hosting)
- **HTML5, CSS3, Bootstrap** (basic front-end)

---

## Requirements

- Python 3 installed
- Git installed
- Virtual environment set up (venv)

---

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```
2. Create and activate the virtual environment:
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # Windows (Git Bash)
   # or source venv/bin/activate  # Linux/macOS
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set environment variables (if needed):
   ```bash
   export FLASK_APP=app.py
   export FLASK_ENV=development
   ```

---

## Running the Application

With the virtual environment active, run:
```bash
flask run
```
Then open `http://127.0.0.1:5000` in your web browser.

---

## Project Structure

```
Evento-Promotion-System/
├── app.py
├── requirements.txt
├── venv/               # Virtual environment
├── templates/          # HTML templates
│   ├── base.html
│   ├── index.html
│   └── events.html
├── static/             # Static files (CSS, images)
└── README.md           # Project documentation
```

---

## Contributing

Contributions are welcome! To contribute:

1. Fork this repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m "Add feature description"`
4. Push to the branch: `git push origin feature-name`
5. Open a Pull Request

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

Bruno Henses – [brunohenses@example.com](mailto:brunohenses@example.com)

Project link: [https://github.com/brunohenses/Extensao_I](https://github.com/brunohenses/Extensao_I)

