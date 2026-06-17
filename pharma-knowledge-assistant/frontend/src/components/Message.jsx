function Message({ message }) {

    const isUser =
        message.type === "user";

    return (

        <div
            style={{
                display: "flex",
                justifyContent:
                    isUser
                        ? "flex-end"
                        : "flex-start",
                marginBottom: "20px"
            }}
        >

            <div
                style={{
                    backgroundColor:
                        isUser
                            ? "#2563eb"
                            : "#ffffff",

                    color:
                        isUser
                            ? "white"
                            : "#1f2937",

                    padding: "14px 16px",

                    borderRadius:
                        "16px",

                    maxWidth: "75%",

                    boxShadow:
                        "0 2px 8px rgba(0,0,0,0.08)",

                    border:
                        isUser
                            ? "none"
                            : "1px solid #e5e7eb"
                }}
            >

                <div
                    style={{
                        fontSize: "14px",
                        lineHeight: "1.6"
                    }}
                >
                    {message.text}
                </div>

                {
                    message.sources &&
                    message.sources.length > 0 && (

                        <div
                            style={{
                                marginTop: "12px",
                                paddingTop: "10px",
                                borderTop:
                                    "1px solid #d1d5db",
                                fontSize: "12px",
                                color: "#6b7280"
                            }}
                        >

                            <strong>
                                📚 Sources
                            </strong>

                            {
                                message.sources.map(
                                    (
                                        source,
                                        index
                                    ) => (

                                        <div
                                            key={index}
                                            style={{
                                                marginTop:
                                                    "6px"
                                            }}
                                        >

                                            📄
                                            {" "}
                                            {
                                                source.document
                                            }

                                            {
                                                source.page &&
                                                (
                                                    <>
                                                        {" "}
                                                        |
                                                        {" "}
                                                        Page
                                                        {" "}
                                                        {
                                                            source.page
                                                        }
                                                    </>
                                                )
                                            }

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