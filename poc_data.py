import os
import random

test_directory = "test_emails"
email_categories = {
    "interested": 10,
    "neutral": 10,
    "not interested": 10
}

def generate_email_content(category):
    greetings = ["Dear Team,", "Hello,", "Hi there,", "Greetings,"]
    sign_offs = ["Best regards,", "Sincerely,", "Cheers,", "Kind regards,"]

    body_interested = [
        # Expanded interested cases
        "I've gone through your proposal and I must say, it's exactly what we've been looking for. Let's schedule a call.",
        "The solutions you're offering seem like a perfect match for our current challenges. Can we have a detailed discussion?",
        "I am really enthusiastic about the possibilities of working together. What are the next steps from here?",
        "Your insights into our sector were spot on. We are keen to explore how we can work together.",
        "Your vision aligns closely with our business objectives. It would be great to understand more about your pricing structure.",
        "The innovation you bring to the table is impressive. Can you send over a formal proposal so we can move this forward?",
        "We're currently looking for exactly these kinds of services. Could you provide case studies or examples of similar work?",
        "Your presentation sparked a lot of discussions here. We're interested in a trial to see how it goes.",
        "Can you tailor your services to our needs? If so, we see a lot of potential for a partnership.",
        "We were discussing finding a solution like yours just recently. Let's set up a demo session.",
        "Your proposal caught my attention. I'd like to hear more.",
        "I'm positively inclined towards your offer. Please provide further details.",
        "Your idea resonates with our goals. Can we discuss this soon?",
        "I see great potential in this partnership. Let's explore further.",
        "Your approach is exactly what we've been looking for. Excited to talk more!",
        "I found your proposal intriguing and would love to learn more.",
        "Your product seems to fit our needs. Can we discuss this in detail?",
        "I'm very interested in your services. Please send more information.",
        "This sounds great! Let's set up a meeting to discuss further.",
        "I'm impressed by what I've seen. What are the next steps?"
    ]


    body_neutral = [
        # Expanded neutral cases
        "We've received your proposal and are currently in the process of evaluation. We'll reach out if it aligns with our plans.",
        "Your offer seems interesting, but it's not a priority for us right now. We'll keep it in mind for future needs.",
        "I'm in the middle of something and can't look into this right now. Can you follow up in a month?",
        "We're not in the market for new solutions currently, but I'd like to revisit this conversation in a few quarters.",
        "It's an interesting proposition, but without more concrete ROI figures, I can't take this to my team.",
        "Can you provide a demo or a trial period? We would like to assess the practicality before making any decisions.",
        "This could potentially be of interest. Let's touch base in the next fiscal when we have more budget flexibility.",
        "I'm forwarding your information to the relevant department. They will get back to you if there's an interest.",
        "We have a few projects closing soon. Let's reconnect once we have more bandwidth.",
        "I see where you're coming from, but I'm not sure how this fits into our current strategy. Let me give it some thought.",
        "Your proposal is interesting. I will get back to you after some deliberation.",
        "I am somewhat intrigued by your offer, but I need more time to decide.",
        "I've received your information and will review it soon.",
        "Your email is noted. We are currently exploring a few options.",
        "This might be something we're interested in. I'll confirm in a few days.",
        "Thank you for your email. I'll review and get back to you.",
        "Can you provide more details? I need to consider this further.",
        "I received your email, and I will think about it and respond soon.",
        "This is interesting, but I need some time to look into it.",
        "I'll need to discuss this with my team before making a decision."
    ]


    body_not_interested = [
        # Additional expanded not interested cases
        "We've given it some thought and have to decline your offer at this time.",
        "It's not quite what we're looking for right now, but thank you for considering us.",
        "Our priorities have shifted, and unfortunately, this doesn't fit in our current agenda.",
        "We did a detailed review and it's not a match for our current strategy. Best of luck!",
        "Thank you for your detailed proposal, but we will not be moving forward with it.",
        "We appreciate your interest in working with us, but it's not a good fit at this stage.",
        "Our needs in this area are already met by a current provider, so we'll pass for now.",
        "This isn't something we are prepared to invest in at this point in time.",
        "We're consolidating our existing tools and services, so we can't accommodate your offer.",
        "Your proposal was clear and well-presented, but it's not what we need at the moment.",
        "While your offering is impressive, it's not aligned with our current focus areas.",
        "While we appreciate the effort you've put into this, it doesn't align with our current strategy.",
        "We are overhauling our systems, and unfortunately, what you're offering doesn't fit into our new model.",
        "Our focus areas have shifted, and at this point, we are not looking to invest in such solutions.",
        "Thank you for reaching out, but we are currently under contractual obligations with a similar provider.",
        "We've reviewed your materials and decided that it isn't the right time for us to embark on this kind of initiative.",
        "Our budget has been earmarked for other projects this year, so we won't be able to consider your proposal.",
        "We're going in a different direction and this doesn't fit into our long-term plans.",
        "We've recently committed to a competitor's product that serves a similar purpose.",
        "Our team doesn't have the capacity to take on new projects at the moment.",
        "After reviewing, we have concluded that your product doesn't meet our specific needs right now.",
        "Thank you for the information, but we're not interested at the moment.",
        "This doesn't align with our current needs, but I'll keep your details.",
        "Unfortunately, we have to pass on this opportunity.",
        "We are not looking to purchase or invest in new solutions right now.",
        "I don't think this is what we need at the moment."
    ]


    email_body = ""
    if category == "interested":
        email_body = random.choice(body_interested)
    elif category == "neutral":
        email_body = random.choice(body_neutral)
    else:  # not interested
        email_body = random.choice(body_not_interested)

    return f"{random.choice(greetings)}\n\n{email_body}\n\n{random.choice(sign_offs)}"

def handle_existing_directory():
    choice = input("Testing directory is populated. Choose an option:\n"
                   "1) Keep current testing emails\n"
                   "2) Keep current emails and add more emails for testing\n"
                   "3) Remove current testing emails and replace them\n"
                   "Enter choice (1, 2, 3): ")

    if choice == "1":
        return  # Keep current emails
    elif choice == "2":
        # Count existing files and adjust the number of new files to generate
        existing_counts = {cat: 0 for cat in email_categories}
        for filename in os.listdir(test_directory):
            for cat in email_categories:
                if filename.startswith(cat):
                    existing_counts[cat] += 1
        for cat in email_categories:
            email_categories[cat] = max(0, email_categories[cat] - existing_counts[cat])
    elif choice == "3":
        # Clear the directory
        for filename in os.listdir(test_directory):
            os.remove(os.path.join(test_directory, filename))

def create_test_emails():
    if os.path.exists(test_directory):
        handle_existing_directory()
    else:
        os.makedirs(test_directory)

    for category, count in email_categories.items():
        for i in range(count):
            filename = f"{test_directory}/{category}_{i+1}.txt"
            try:
                content = generate_email_content(category)
                with open(filename, 'w') as file:
                    file.write(content)
                print(f"Generated {filename}")
            except Exception as e:
                print(f"Error generating file {filename}: {e}")

if __name__ == "__main__":
    create_test_emails()
