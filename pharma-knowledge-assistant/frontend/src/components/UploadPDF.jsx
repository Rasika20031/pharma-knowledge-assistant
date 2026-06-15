import { useState } from "react";
import API from "../services/api";

function UploadPDF() {

    const [file, setFile] = useState(null);
    const [message, setMessage] = useState("");

    const uploadFile = async () => {

        if (!file) {
            setMessage("Please select a PDF");
            return;
        }

        const formData = new FormData();

        formData.append(
            "file",
            file
        );

        try {

            const response = await API.post(
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
                response.data.message
            );

        } catch (error) {

            console.error(error);

            setMessage(
                "Upload failed"
            );
        }
    };

    return (
        <div>

            <h2>Upload PDF</h2>

            <input
                type="file"
                accept=".pdf"
                onChange={(e) =>
                    setFile(e.target.files[0])
                }
            />

            <button onClick={uploadFile}>
                Upload
            </button>

            <p>{message}</p>

        </div>
    );
}

export default UploadPDF;