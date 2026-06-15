import { useEffect, useRef } from "react";
import Message from "./Message";

function ChatWindow({
    messages,
    loading
}) {

    const bottomRef = useRef(null);

    useEffect(() => {

        bottomRef.current?.scrollIntoView({
            behavior: "smooth"
        });

    }, [messages, loading]);

    return (

        <div
            style={{
                height: "500px",
                overflowY: "auto",
                border: "1px solid #ddd",
                borderRadius: "12px",
                padding: "20px",
                marginBottom: "20px",
                backgroundColor: "#fafafa"
            }}
        >

            {
                messages.length === 0 &&
                !loading && (

                    <div
                        style={{
                            textAlign: "center",
                            marginTop: "150px",
                            color: "gray"
                        }}
                    >

                        Ask a question about your uploaded documents.

                    </div>

                )
            }

            {
                messages.map(
                    (
                        message,
                        index
                    ) => (

                        <Message
                            key={index}
                            message={message}
                        />

                    )
                )
            }

            {
                loading && (

                    <div
                        style={{
                            display: "flex",
                            justifyContent:
                                "flex-start",
                            marginBottom: "15px"
                        }}
                    >

                        <div
                            style={{
                                backgroundColor:
                                    "#f1f5f9",
                                padding: "12px",
                                borderRadius:
                                    "12px"
                            }}
                        >

                            🤖 Thinking...

                        </div>

                    </div>

                )
            }

            <div ref={bottomRef} />

        </div>

    );
}

export default ChatWindow;