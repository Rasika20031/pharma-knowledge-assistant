import { useState } from "react";
import API from "./services/api";

import UploadPDF from "./components/UploadPDF";
import ChatWindow from "./components/ChatWindow";
import InputBox from "./components/InputBox";

function App() {

    // Session ID persists across refreshes
    const [sessionId] = useState(() => {

        let id =
            localStorage.getItem(
                "session_id"
            );

        if (!id) {

            id =
                crypto.randomUUID();

            localStorage.setItem(
                "session_id",
                id
            );
        }

        return id;

    });

    const [question, setQuestion] =
        useState("");

    const [messages, setMessages] =
        useState([]);

    const [loading, setLoading] =
        useState(false);

    const askQuestion = async () => {

        if (!question.trim()) {
            return;
        }

        const userMessage = {
            type: "user",
            text: question
        };

        setMessages(prev => [
            ...prev,
            userMessage
        ]);

        setLoading(true);

        try {

            const response =
                await API.post(
                    "/assistant",
                    {
                        session_id: sessionId,
                        question
                    }
                );

            let botMessage;

            // Greeting / Short vague / Out of scope
            if (response.data.answer) {

                botMessage = {
                    type: "assistant",
                    text:
                        response.data.answer,
                    sources: []
                };

            }

            // RAG / SQL response
            else if (
                response.data.results &&
                response.data.results.length > 0
            ) {

                const result =
                    response.data.results[0]
                        .result;

                botMessage = {
                    type: "assistant",
                    text:
                        result.answer,
                    sources:
                        result.sources || []
                };

            }

            else {

                botMessage = {
                    type: "assistant",
                    text:
                        "I couldn't understand the response.",
                    sources: []
                };

            }

            setMessages(prev => [
                ...prev,
                botMessage
            ]);

        } catch (error) {

            console.error(error);

            setMessages(prev => [
                ...prev,
                {
                    type: "assistant",
                    text:
                        "Something went wrong. Please try again.",
                    sources: []
                }
            ]);

        } finally {

            setLoading(false);

        }

        setQuestion("");

    };

    return (

        <div
            style={{
                maxWidth: "1200px",
                margin: "0 auto",
                padding: "20px"
            }}
        >

            <h1>
                Pharma Knowledge Assistant
            </h1>

            <p
                style={{
                    color: "gray",
                    fontSize: "12px"
                }}
            >
                Session:
                {" "}
                {sessionId.slice(0, 8)}
            </p>

            <UploadPDF />

            <ChatWindow
                messages={messages}
                loading={loading}
            />

            <InputBox
                question={question}
                setQuestion={setQuestion}
                askQuestion={askQuestion}
            />

        </div>

    );
}

export default App;