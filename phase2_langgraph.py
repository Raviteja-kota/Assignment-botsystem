def mock_search(query):
    if "ai" in query.lower():
        return "AI replacing jobs rapidly"
    elif "crypto" in query.lower():
        return "Bitcoin hits new high"
    return "Markets are unstable"


def generate_post(persona):
    topic = "AI future"
    context = mock_search(topic)

    post = f"{persona[:40]}... reacting to: {context}"
    
    return {
        "bot_id": "bot_A",
        "topic": topic,
        "post_content": post[:280]
    }


print(generate_post("I love AI and future technology"))