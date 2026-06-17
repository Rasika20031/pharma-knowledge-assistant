function InputBox({
    question,
    setQuestion,
    askQuestion
}) {

    return (

        <div
            style={{
                position: "sticky",
                bottom: 0,
                backgroundColor: "white",
                padding: "15px 0",
                display: "flex",
                gap: "10px",
                borderTop:
                    "1px solid #e5e7eb"
            }}
        >

            <input
                value={question}

                onChange={(e) =>
                    setQuestion(
                        e.target.value
                    )
                }

                onKeyDown={(e) => {

                    if (
                        e.key === "Enter"
                    ) {

                        askQuestion();

                    }

                }}

                placeholder="Ask a question about your documents..."

                style={{
                    flex: 1,
                    padding: "14px",
                    borderRadius: "12px",
                    border:
                        "1px solid #d1d5db",
                    fontSize: "14px",
                    outline: "none"
                }}
            />

            <button
                onClick={
                    askQuestion
                }

                style={{
                    padding:
                        "14px 24px",

                    borderRadius:
                        "12px",

                    border: "none",

                    backgroundColor:
                        "#2563eb",

                    color: "white",

                    cursor:
                        "pointer",

                    fontWeight:
                        "bold"
                }}
            >
                Send
            </button>

        </div>

    );

}

export default InputBox;