function InputBox({
    question,
    setQuestion,
    askQuestion
}) {

    return (

        <div
            style={{
                display: "flex",
                gap: "10px"
            }}
        >

            <input
                value={question}
                onChange={(e) =>
                    setQuestion(
                        e.target.value
                    )
                }
                placeholder="Ask a question..."
                style={{
                    flex: 1,
                    padding: "12px"
                }}
            />

            <button
                onClick={askQuestion}
            >
                Send
            </button>

        </div>

    );
}

export default InputBox;