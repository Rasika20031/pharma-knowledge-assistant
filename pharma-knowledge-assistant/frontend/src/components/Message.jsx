function Message({ message }) {

    const isUser = message.type === "user";

    return (
        <div
            style={{
                display: "flex",
                justifyContent: isUser
                    ? "flex-end"
                    : "flex-start",
                marginBottom: "15px"
            }}
        >
            <div
                style={{
                    backgroundColor: isUser
                        ? "#2563eb"
                        : "#f1f5f9",
                    color: isUser
                        ? "white"
                        : "black",
                    padding: "12px",
                    borderRadius: "12px",
                    maxWidth: "70%"
                }}
            >
                <div>
                    {message.text}
                </div>

                {
                    message.sources &&
                    message.sources.length > 0 && (

                        <div
                            style={{
                                marginTop: "10px",
                                fontSize: "12px"
                            }}
                        >

                            <strong>
                                Sources
                            </strong>

                            {
                                message.sources.map(
                                    (
                                        source,
                                        index
                                    ) => (

                                        <div key={index}>
                                            📄 {source.document}
                                            {" | "}
                                            Page {source.page}
                                        </div>

                                    )
                                )
                            }

                        </div>

                    )
                }

            </div>
        </div>
    );
}

export default Message;