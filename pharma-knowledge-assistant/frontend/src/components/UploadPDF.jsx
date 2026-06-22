import { useState } from "react";
import API from "../services/api";

function UploadPDF() {

    const [files, setFiles] =
        useState([]);

    const [message, setMessage] =
        useState("");

    const uploadFile = async () => {

        if (
            files.length === 0
        ) {

            setMessage(
                "⚠️ Please select PDF files."
            );

            return;
        }

        const formData =
            new FormData();

        for (
            let i = 0;
            i < files.length;
            i++
        ) {

            formData.append(
                "files",
                files[i]
            );

        }

        try {

            const response =
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
                `✅ ${response.data.uploaded_files.length} PDF(s) uploaded successfully!`
            );

        } catch (error) {

            console.error(
                error
            );

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
                📄 Upload PDFs
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

                    multiple

                    onChange={(e) =>
                        setFiles(
                            Array.from(
                                e.target.files
                            )
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
                files.length > 0 && (

                    <div
                        style={{
                            marginTop:
                                "10px",

                            color:
                                "#6b7280"
                        }}
                    >

                        <strong>
                            Selected:
                        </strong>

                        {
                            files.map(
                                (
                                    file,
                                    index
                                ) => (

                                    <div
                                        key={
                                            index
                                        }
                                    >
                                        📄
                                        {" "}
                                        {
                                            file.name
                                        }
                                    </div>

                                )
                            )
                        }

                    </div>

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