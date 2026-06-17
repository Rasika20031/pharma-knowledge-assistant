import { useState } from "react";
import API from "../services/api";

function UploadPDF() {

    const [file, setFile] =
        useState(null);

    const [message, setMessage] =
        useState("");

    const uploadFile = async () => {

        if (!file) {

            setMessage(
                "⚠️ Please select a PDF file."
            );

            return;
        }

        const formData =
            new FormData();

        formData.append(
            "file",
            file
        );

        try {

            await API.post(
                "/upload",
                formData,
                {
                    headers: {
                        "Content-Type":
                            "multipart/form-data"
                    }
                }
            );

            setMessage(
                `✅ ${file.name} uploaded successfully!`
            );

        } catch (error) {

            console.error(error);

            setMessage(
                "❌ Upload failed. Please try again."
            );
        }

    };

    return (

        <div
            style={{
                backgroundColor:
                    "#ffffff",

                border:
                    "1px solid #e5e7eb",

                borderRadius:
                    "12px",

                padding:
                    "20px",

                marginBottom:
                    "20px",

                boxShadow:
                    "0 2px 8px rgba(0,0,0,0.05)"
            }}
        >

            <h3
                style={{
                    marginTop: 0
                }}
            >
                📄 Upload PDF
            </h3>

            <div
                style={{
                    display: "flex",
                    gap: "10px",
                    alignItems:
                        "center"
                }}
            >

                <input
                    type="file"
                    accept=".pdf"

                    onChange={(e) =>
                        setFile(
                            e.target.files[0]
                        )
                    }
                />

                <button
                    onClick={
                        uploadFile
                    }

                    style={{
                        backgroundColor:
                            "#2563eb",

                        color:
                            "white",

                        border:
                            "none",

                        padding:
                            "10px 18px",

                        borderRadius:
                            "8px",

                        cursor:
                            "pointer"
                    }}
                >
                    Upload
                </button>

            </div>

            {
                file && (

                    <p
                        style={{
                            color:
                                "#6b7280",
                            marginTop:
                                "10px"
                        }}
                    >
                        Selected:
                        {" "}
                        <strong>
                            {file.name}
                        </strong>
                    </p>

                )
            }

            {
                message && (

                    <p
                        style={{
                            marginTop:
                                "12px",

                            fontWeight:
                                "500"
                        }}
                    >
                        {message}
                    </p>

                )
            }

        </div>

    );

}

export default UploadPDF;