import os 
from dotenv import load_dotenv

from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


from langchain.agents import create_agent
from langchain_openrouter import ChatOpenRouter
from langchain.tools import tool 


llm = ChatOpenRouter(
    model = "openai/gpt-oss-20b:free",
    api_key = OPENROUTER_API_KEY
)

from langchain.tools import tool

@tool
def get_info() -> dict:
    """
    Returns structured information about Umamaheshwara Reddy.
    Use this tool whenever the user asks about his profile, education,
    skills, projects, experience, certifications, contact details,
    or career objectives.
    """

    return {
        "name": "Umamaheshwara Reddy",
        "title": "AI/ML Engineer & Full-Stack Developer",

        "summary": (
        "B.Tech graduate in Computer Science and Engineering (AI & ML) "
        "from Alliance University, Bengaluru, passionate about building "
        "AI-powered applications, machine learning solutions, and "
        "full-stack web applications."
        ),

        "education": {
            "degree": "B.Tech in Computer Science and Engineering (AI & ML)",
            "university": "Alliance University",
            "cgpa": "8.3",
            "graduation": "2026",
            "status": "Graduated",
            "location": "Bengaluru"
        },

        "skills": {
            "languages": [
                "Python",
                "Java"
            ],
            "core_cs": [
                "Data Structures",
                "Algorithms",
                "Object-Oriented Programming"
            ],
            "databases": [
                "MySQL",
                "MongoDB",
                "MongoDB Atlas"
            ],
            "ai_ml": [
                "Machine Learning",
                "Deep Learning",
                "TensorFlow",
                "Scikit-learn",
                "NumPy",
                "Pandas",
                "PySpark",
                "Seaborn",
                "Reinforcement Learning"
            ],
            "web": [
                "HTML5",
                "Tailwind CSS",
                "JavaScript",
                "REST APIs",
                "Flask",
                "Django"
            ],
            "cloud": [
                "AWS EC2",
                "Git",
                "GitHub",
                "Vercel"
            ]
        },

        "projects": [
            {
                "name": "AI-Driven Energy Management System",
                "description": "Developed a hybrid XGBoost-LSTM forecasting system integrated with Deep Q-Network reinforcement learning for energy demand prediction and microgrid optimization.",
                "technologies": [
                    "XGBoost",
                    "LSTM",
                    "Deep Reinforcement Learning",
                    "Django"
                ]
            },
            {
                "name": "Farmfinity - Crop Recommendation System",
                "description": "Built an AI web application that recommends suitable crops using soil nutrients, weather, and environmental conditions.",
                "technologies": [
                    "Random Forest",
                    "Neural Networks",
                    "Django"
                ]
            },
            {
                "name": "Real Estate Websites",
                "description": "Designed and deployed responsive websites for construction and real estate businesses with modern UI and lead generation features.",
                "technologies": [
                    "HTML",
                    "CSS",
                    "JavaScript",
                    "Vercel"
                ]
            }
        ],

        "experience": [
            {
                "role": "Freelance Web Developer",
                "company": "Sreevaari Homes & Golden Towers",
                "duration": "Jun 2025 - Aug 2025",
                "responsibilities": [
                    "Designed responsive websites",
                    "Developed interactive UI",
                    "Implemented inquiry forms",
                    "Deployed custom domains"
                ]
            }
        ],

        "certifications": [
            "Oracle Generative AI",
            "Oracle AI Fundamentals",
            "Coursera Data Structures"
        ],

        "achievements": {
            "ai_projects": 5,
            "ai_certifications": 2,
            "cgpa": 8.3,
            "twelfth_percentage": "90%"
        },

        "career_goal": (
            "Seeking full-time opportunities in AI/ML, Data Science, "
            "and Software Development."
        ),

        "contact": {
            "email": "uma932244@gmail.com",
            "phone": "+91-9606179178",
            "location": "Bengaluru, Karnataka, India"
        }
    }
model = create_agent(
    model = llm,
    tools = [get_info],
    system_prompt = "You are a Umamaheshwara Reddy's Assistant"
    )

@app.route("/")
def home():
    return render_template("index.html")

@ app.route("/chat", methods = ["POST"])
def chat():
    data = request.get_json()
    query = data["query"]

    res = model.invoke({"messages": [{
        "role": "user",
        "content": query
    }]})

    return jsonify({"text": res["messages"][-1].content})

if __name__ == "__main__":
    app.run(debug=True)
