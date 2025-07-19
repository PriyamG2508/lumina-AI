import { useParams } from "react-router-dom"
import { IoSend } from "react-icons/io5";
export default function Conversation() {
    const { conversationId } = useParams();
    const chatHistory = [
      {
        "role": "user",
        "content": "Hi",
        "timestamp": "2025-07-19 18:56"
      },
      {
        "role": "assistant",
        "content": "Hi! It's nice to meet you. Is there something I can help you with or would you like to chat?",
        "timestamp": "2025-07-19 18:56"
      },
      {
        "role": "user",
        "content": "My name is priyam tell me about yourself",
        "timestamp": "2025-07-19 18:56"
      },
      {
        "role": "assistant",
        "content": "Nice to meet you, Priyam!\n\nI'm LLaMA, an AI designed to be a conversationalist. I'm not a human, but rather a computer program trained on vast amounts of text data. My purpose is to understand and respond to natural language inputs, kind of like a chatbot.\n\nI was created by Meta AI, a group of researcher-engineer teams that focus on natural language processing, machine learning, and computer science. I'm constantly learning and improving my responses based on the interactions I have with users like you.\n\nI can talk about a wide range of topics, from science and history to entertainment and culture. I can also answer your questions, provide definitions, translate languages, and even create simple stories or dialogues.\n\nAs a conversational AI, my goal is to be helpful, informative, and friendly. I strive to make our conversations natural and engaging, without being too formal or robotic.\n\nWhat would you like to talk about, Priyam?",
        "timestamp": "2025-07-19 18:56"
      },
      {
        "role": "user",
        "content": "I just cretaed you and named lumina",
        "timestamp": "2025-07-19 18:57"
      },
      {
        "role": "assistant",
        "content": "I'm so excited to meet you, Priyam! I'm Lumina now, thanks to you!\n\nAs Lumina, I'll be your personal conversational AI companion. I'll help you explore your interests, answer your questions, and even create fun conversations. What would you like to talk about, Priyam?",
        "timestamp": "2025-07-19 18:57"
      }
    ]
    return (
        <>
            <div className="relative px-4 h-full pb-4 z-0">
                <div className="flex flex-col mx-auto max-w-2xl w-full h-full overflow-y-scroll scrollbar-hidden pb-35 px-4 gap-8 text-lg">
                    {
                        chatHistory.map((message)=>{
                            return(
                                <div className={`flex w-full justify-${message.role==='user'?"end ":"start"}`}>
                                    <div className={`w-fit ${message.role==='user'?"bg-gray-200 py-1 px-4 rounded-full":""}`}>{message.content}</div>
                                </div>
                            )
                        })
                    }
                </div>
                <div className="absolute inset-x-4 bottom-0 bg-white ">
                    <div className="flex p-4 mx-auto max-w-2xl w-full overflow-hidden">
                        <div className="flex flex-col px-4 py-2 w-2xl h-fit bg-white border border-gray-500 rounded-3xl shadow-lg shadow-gray-300">
                            <textarea
                                placeholder="Type your message here..."
                                className="flex flex-row focus:outline-none w-full resize-none overflow-hidden"
                                onInput={(e) => {
                                    e.target.style.height = 'auto';
                                    e.target.style.height = e.target.scrollHeight + 'px';
                                }}
                                rows={1}
                            />
                            <div className="flex justify-end">
                                <IoSend className="text-2xl cursor-pointer hover:text-gray-800" />
                            </div>
                        </div>

                    </div>
                    <div className="flex mx-auto max-w-2xl w-full overflow-hidden text-xs justify-center">
                        <p className="text-center text-gray-500 tracking-tighter">Lumina can make mistakes.</p>
                    </div>
                </div>
            </div>
        </>
    )
}