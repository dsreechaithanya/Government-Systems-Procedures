"""Interactive, jurisdiction-neutral course on government systems and procedures."""

from __future__ import annotations

from typing import Any


COURSE: list[dict[str, Any]] = [
    {
        "title": "Government organization and hierarchy",
        "sections": [
            (
                "How to read an organization",
                "Start with the legal or constitutional basis for the institution. "
                "Then map the political leadership, administrative leadership, "
                "divisions, offices, and service-delivery units. Names and reporting "
                "lines differ between jurisdictions.",
            ),
            (
                "Roles and accountability",
                "Separate policy direction from administration and operational "
                "delivery. For each role, identify its decision authority, reporting "
                "line, delegated powers, and accountability or oversight mechanism.",
            ),
            (
                "Build a department map",
                "Use the department's current official organization chart and mandate. "
                "Record each unit's responsibilities, the office it reports to, and "
                "the public services it supports. Confirm the chart's publication "
                "date because structures can change.",
            ),
        ],
        "activity": "Draw a one-page reporting chart for a service in your department. "
        "Mark who sets policy, who approves decisions, and who delivers the service.",
        "questions": [
            {
                "question": "What is the best starting point for mapping a public body's structure?",
                "options": [
                    "An unofficial online discussion",
                    "Its current official mandate and organization chart",
                    "A chart from a different department",
                    "An assumed chain of command",
                ],
                "answer": 1,
                "explanation": "Current official documents are the most reliable way to "
                "confirm a body's mandate and reporting lines.",
            },
            {
                "question": "Why should policy, administration, and service delivery be distinguished?",
                "options": [
                    "They always belong to different ministries",
                    "It clarifies responsibilities and decision authority",
                    "It removes the need for oversight",
                    "It means staff do not need written procedures",
                ],
                "answer": 1,
                "explanation": "Distinguishing these functions helps identify who is "
                "responsible for each decision and outcome.",
            },
            {
                "question": "What should you do before relying on an organization chart?",
                "options": [
                    "Assume it is permanent",
                    "Check that it is current and from an official source",
                    "Replace it with a chart from memory",
                    "Ignore its publication date",
                ],
                "answer": 1,
                "explanation": "Department structures and delegated responsibilities can change.",
            },
        ],
    },
    {
        "title": "Administrative procedures and protocols",
        "sections": [
            (
                "Follow the approved process",
                "Use the applicable written procedure, forms, delegations, and records "
                "requirements. Check which version is in force and whether the matter "
                "requires review, approval, consultation, or escalation.",
            ),
            (
                "A reliable case workflow",
                "A common workflow is to receive and register a request, check "
                "completeness and authority, assess it against applicable criteria, "
                "obtain required advice or approvals, communicate a reasoned outcome, "
                "and retain the record under the records schedule.",
            ),
            (
                "Fairness and records",
                "Apply published criteria consistently, protect personal and "
                "confidential information, keep an auditable record of decisions, "
                "and explain review or appeal routes where the applicable rules "
                "provide them.",
            ),
        ],
        "activity": "Choose a routine request handled by your office. List its stages, "
        "the responsible role at each stage, required records, and any escalation point.",
        "questions": [
            {
                "question": "What is a sound first step when handling an official request?",
                "options": [
                    "Skip registration if it looks routine",
                    "Register it and check the applicable procedure and authority",
                    "Promise approval before reviewing it",
                    "Use an outdated form to save time",
                ],
                "answer": 1,
                "explanation": "Registration and an initial authority and procedure check "
                "support traceability and correct handling.",
            },
            {
                "question": "Why retain a record of a decision?",
                "options": [
                    "To make the process impossible to review",
                    "To support accountability, continuity, and audit",
                    "To replace the need for a reasoned decision",
                    "To share confidential information more widely",
                ],
                "answer": 1,
                "explanation": "An appropriate record helps explain what was decided, "
                "why, and under whose authority.",
            },
            {
                "question": "What should staff do if a case exceeds their delegated authority?",
                "options": [
                    "Approve it anyway",
                    "Escalate it through the approved channel",
                    "Delete the request",
                    "Ask an unrelated office to decide informally",
                ],
                "answer": 1,
                "explanation": "Decisions should be made by an authorized role or "
                "escalated using the applicable process.",
            },
        ],
    },
    {
        "title": "Acts, rules, and regulations",
        "sections": [
            (
                "Understand the instrument",
                "An Act or equivalent primary legislation may establish powers, duties, "
                "and institutions. Regulations, rules, orders, or directives may set "
                "more detailed requirements when authorized by the relevant law. "
                "Terminology and legal effect vary by jurisdiction.",
            ),
            (
                "Verify before applying",
                "Use an official legal publication or government source. Check the "
                "instrument's exact title, current version, commencement date, "
                "amendments, transitional provisions, and any guidance issued by "
                "the responsible authority.",
            ),
            (
                "Apply with care",
                "Identify the provision that gives the office its authority and the "
                "criteria that govern the decision. Do not treat informal summaries "
                "as binding law. Refer uncertainty or legal interpretation questions "
                "to the department's authorized legal or policy adviser.",
            ),
        ],
        "activity": "Select one law or rule relevant to your work. Record its official "
        "title, source, current version, key provisions, and the official guidance "
        "that explains how your department applies it.",
        "questions": [
            {
                "question": "Where should you confirm the current text of an applicable law?",
                "options": [
                    "An official legal publication or government source",
                    "An undated personal note",
                    "A social media post",
                    "A document for a different jurisdiction",
                ],
                "answer": 0,
                "explanation": "An official source helps verify the authoritative text "
                "and its current status.",
            },
            {
                "question": "Which details can matter when checking a legal instrument?",
                "options": [
                    "Only its short name",
                    "Its version, commencement, amendments, and transitional provisions",
                    "The color of its cover",
                    "Whether it appears in an unofficial summary",
                ],
                "answer": 1,
                "explanation": "These details can affect which provisions apply and when.",
            },
            {
                "question": "What should you do when the legal meaning is uncertain?",
                "options": [
                    "Guess based on a similar case",
                    "Seek advice from an authorized legal or policy adviser",
                    "Ignore the relevant provision",
                    "Treat an informal summary as binding",
                ],
                "answer": 1,
                "explanation": "Legal interpretation should be referred to the "
                "department's authorized advisers.",
            },
        ],
    },
    {
        "title": "Budgeting and public financial management",
        "sections": [
            (
                "Understand the budget cycle",
                "A typical cycle includes strategic planning, estimating costs and "
                "revenues, budget preparation and approval, execution, monitoring, "
                "financial reporting, audit, and evaluation. The calendar and "
                "approval bodies depend on the jurisdiction.",
            ),
            (
                "Manage funds responsibly",
                "Use appropriated funds only for authorized purposes and within "
                "approved limits. Follow applicable procurement and commitment "
                "controls, document approvals, reconcile records, and report "
                "variances promptly.",
            ),
            (
                "Connect spending to outcomes",
                "A proposal should explain the public need, options considered, "
                "estimated full cost, funding source, risks, expected outputs and "
                "outcomes, and how results will be measured. Distinguish allocated "
                "funds from actual spending.",
            ),
        ],
        "activity": "For a proposed activity, outline its objective, cost assumptions, "
        "funding source, approval path, procurement needs, risks, and measurable results.",
        "questions": [
            {
                "question": "Which sequence best describes a typical public budget cycle?",
                "options": [
                    "Audit only, then no further review",
                    "Plan, prepare and approve, execute, monitor, report, and evaluate",
                    "Spend first and seek approval later",
                    "Procure without a budget",
                ],
                "answer": 1,
                "explanation": "Budget management spans planning through execution, "
                "reporting, audit, and evaluation.",
            },
            {
                "question": "How should public funds be used?",
                "options": [
                    "For any purpose that seems useful",
                    "Only for authorized purposes and within approved limits",
                    "Without keeping approval records",
                    "Outside applicable procurement controls",
                ],
                "answer": 1,
                "explanation": "Public expenditure must follow the applicable "
                "authorization, limit, and control requirements.",
            },
            {
                "question": "What is useful evidence that a funded activity achieved its purpose?",
                "options": [
                    "A measurable result linked to the activity's objective",
                    "An unverified estimate of money spent",
                    "A list of meetings only",
                    "An undocumented verbal assurance",
                ],
                "answer": 0,
                "explanation": "Results should be measured against the activity's "
                "stated objectives, not spending alone.",
            },
        ],
    },
    {
        "title": "Government schemes and programs",
        "sections": [
            (
                "Know the program",
                "Start with the program's official guidelines, eligibility criteria, "
                "responsible authority, geographic or population scope, application "
                "process, benefits, funding conditions, and review or grievance routes.",
            ),
            (
                "Support fair access",
                "Use the published criteria consistently. Explain required documents, "
                "deadlines, and available assistance in accessible language. Protect "
                "applicant information and provide a clear route for questions or "
                "complaints under the applicable process.",
            ),
            (
                "Track delivery and results",
                "Monitor applications, decisions, delivery times, expenditure, "
                "coverage, and outcomes using approved measures. Look for barriers "
                "or uneven access, and report implementation issues to the "
                "responsible program authority.",
            ),
        ],
        "activity": "Choose a program relevant to your work. Summarize its official "
        "eligibility rules, application path, responsible office, benefits, "
        "complaint route, and outcome measures.",
        "questions": [
            {
                "question": "What is the best source for a program's eligibility criteria?",
                "options": [
                    "Current official program guidelines",
                    "A previous applicant's guess",
                    "An unrelated program's brochure",
                    "An unofficial rumor",
                ],
                "answer": 0,
                "explanation": "Official, current guidelines set out the program's "
                "authoritative criteria.",
            },
            {
                "question": "How should staff assess applications?",
                "options": [
                    "Apply published criteria consistently",
                    "Use different unpublished rules for each applicant",
                    "Decide based on personal familiarity",
                    "Skip required documentation checks",
                ],
                "answer": 0,
                "explanation": "Consistent use of published criteria supports fair and "
                "accountable program delivery.",
            },
            {
                "question": "Which measure helps assess whether a program is working?",
                "options": [
                    "Outcomes measured against the program's objectives",
                    "The number of informal conversations",
                    "The size of its publicity materials",
                    "An unsupported impression",
                ],
                "answer": 0,
                "explanation": "Outcome measures should connect to the program's "
                "stated objectives.",
            },
        ],
    },
    {
        "title": "Inter-departmental coordination and communication",
        "sections": [
            (
                "Agree on the purpose",
                "For joint work, establish the shared outcome, each department's "
                "mandate and lead role, decision rights, milestones, dependencies, "
                "and escalation route. Record agreements and unresolved issues.",
            ),
            (
                "Communicate clearly",
                "Use agreed channels and named contacts. Share concise, accurate "
                "updates with decisions needed, owners, and due dates. Confirm "
                "important agreements in writing and maintain a shared action log "
                "or approved record.",
            ),
            (
                "Share information responsibly",
                "Before sharing information, confirm authority, purpose, necessity, "
                "classification, privacy requirements, and the approved channel. "
                "Share only what is needed with authorized recipients and record "
                "important exchanges as required.",
            ),
        ],
        "activity": "For a cross-department task, draft a one-page coordination note "
        "with the shared outcome, lead, roles, decisions, milestones, information "
        "sharing safeguards, and escalation route.",
        "questions": [
            {
                "question": "What should teams agree at the start of joint work?",
                "options": [
                    "Only an informal meeting time",
                    "The shared outcome, roles, decision rights, milestones, and escalation route",
                    "That no department is accountable",
                    "That all decisions remain undocumented",
                ],
                "answer": 1,
                "explanation": "Clear roles and decision paths reduce gaps and "
                "duplication in cross-department work.",
            },
            {
                "question": "Before sharing government information, what should staff check?",
                "options": [
                    "Only whether it is convenient",
                    "Authority, purpose, necessity, privacy, and approved channels",
                    "Whether the recipient is curious",
                    "Nothing if the request is urgent",
                ],
                "answer": 1,
                "explanation": "Information should be shared lawfully, securely, and "
                "only as needed.",
            },
            {
                "question": "What makes a coordination update actionable?",
                "options": [
                    "It identifies the decision needed, owner, and due date",
                    "It omits responsibilities",
                    "It is sent to everyone without regard to authorization",
                    "It avoids recording decisions",
                ],
                "answer": 0,
                "explanation": "Clear actions, owners, and dates support follow-through.",
            },
        ],
    },
]


def show_lesson(index: int) -> None:
    """Display one lesson and its practical activity."""
    lesson = COURSE[index]
    print(f"\n{lesson['title']}")
    print("=" * len(lesson["title"]))
    for heading, body in lesson["sections"]:
        print(f"\n{heading}\n{body}")
    print(f"\nPractical activity\n{lesson['activity']}")


def choose_topic() -> int | None:
    """Prompt for a topic number, returning a zero-based index or None."""
    print("\nChoose a topic:")
    for number, lesson in enumerate(COURSE, start=1):
        print(f"  {number}. {lesson['title']}")
    print("  0. Back")

    while True:
        choice = input("Topic number: ").strip()
        if choice == "0":
            return None
        if choice.isdigit() and 1 <= int(choice) <= len(COURSE):
            return int(choice) - 1
        print(f"Enter a number from 1 to {len(COURSE)}, or 0 to go back.")


def run_quiz(index: int) -> None:
    """Run a topic quiz and report its score."""
    lesson = COURSE[index]
    score = 0
    questions = lesson["questions"]
    print(f"\nQuiz: {lesson['title']}")

    for number, item in enumerate(questions, start=1):
        print(f"\n{number}. {item['question']}")
        for option_number, option in enumerate(item["options"], start=1):
            print(f"  {option_number}. {option}")

        while True:
            answer = input("Your answer (1-4): ").strip()
            if answer.isdigit() and 1 <= int(answer) <= len(item["options"]):
                break
            print(f"Enter a number from 1 to {len(item['options'])}.")

        if int(answer) - 1 == item["answer"]:
            score += 1
            print("Correct.")
        else:
            correct = item["options"][item["answer"]]
            print(f"Not quite. Correct answer: {correct}")
        print(item["explanation"])

    print(f"\nScore: {score}/{len(questions)}")
    if score == len(questions):
        print("Excellent work. Try the practical activity to apply the lesson.")
    elif score >= len(questions) // 2:
        print("Good progress. Review any missed concepts and try again.")
    else:
        print("Review the lesson, then take the quiz again.")


def show_study_plan() -> None:
    """Print a practical sequence for studying the course."""
    print("\nSuggested study plan")
    print("====================")
    print("1. Read one lesson and complete its practical activity.")
    print("2. Use your department's current official documents to verify local details.")
    print("3. Take the lesson quiz and review any missed concepts.")
    print("4. Repeat for each topic, then map how the topics connect in your role.")
    print(
        "\nThis course is a general learning aid, not legal or financial advice. "
        "Government structures, laws, procedures, budgets, and programs differ "
        "by jurisdiction and change over time. Confirm requirements with current "
        "official sources and authorized advisers."
    )


def main() -> None:
    """Run the interactive course."""
    print("Government Systems & Procedures")
    print("A jurisdiction-neutral learning course")
    print("-" * 34)

    while True:
        print(
            "\nMain menu\n"
            "  1. Read a lesson\n"
            "  2. Take a topic quiz\n"
            "  3. View the suggested study plan\n"
            "  4. Exit"
        )
        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            topic = choose_topic()
            if topic is not None:
                show_lesson(topic)
        elif choice == "2":
            topic = choose_topic()
            if topic is not None:
                run_quiz(topic)
        elif choice == "3":
            show_study_plan()
        elif choice == "4":
            print("Thank you for studying. Goodbye.")
            return
        else:
            print("Enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye.")
