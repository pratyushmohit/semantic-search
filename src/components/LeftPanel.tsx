import React, { useCallback, useState } from 'react';
import { FiUpload } from 'react-icons/fi';

const LeftPanel: React.FC = () => {
    const [file, setFile] = useState<File | null>(null);
    const [text, setText] = useState<string>('');

    const onFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        if (e.target.files && e.target.files[0]) {
            setFile(e.target.files[0]);
        }
    };

    const onDrop = useCallback((e: React.DragEvent<HTMLDivElement>) => {
        e.preventDefault();
        if (e.dataTransfer.files && e.dataTransfer.files[0]) {
            setFile(e.dataTransfer.files[0]);
        }
    }, []);

    const onUpload = async () => {
        if (file) {
            const formData = new FormData();
            formData.append('file', file);

            try {
                const response = await fetch('http://localhost:8000/upload-file', {
                    method: 'POST',
                    body: formData
                });
                const data = await response.json();
                console.log(data);
            } catch (error) {
                console.error('Error uploading file:', error);
            }
        }
    };
    return (
        <div className="flex flex-col space-y-8 w-full md:w-1/3 p-10 bg-gradient-to-bl from-purple-100 to-blue-200 rounded-xl shadow-lg">
            
            <div 
                onDrop={onDrop} 
                onDragOver={(e) => e.preventDefault()} 
                className="flex flex-col items-center justify-center p-6 border-4 border-dashed border-purple-300 rounded-xl transition duration-300 ease-in-out hover:border-purple-400 cursor-pointer"
            >
                <input id="file-upload" type="file" className="absolute opacity-0" accept=".csv" onChange={onFileChange} />
                <FiUpload className="text-gray-500 text-2xl mb-2"/>
                <label htmlFor="file-upload" className="text-gray-600 font-medium cursor-pointer hover:text-gray-700 transition">
                    {file ? file.name : 'Drag & Drop or Click to Upload'}
                </label>
            </div>
            
            <div className="flex flex-col space-y-2">
                <label className="text-gray-700 font-medium">Paste Text</label>
                <textarea
                    value={text}
                    onChange={(e) => setText(e.target.value)}
                    className="w-full p-4 border rounded-xl shadow-sm bg-white placeholder-gray-400 transition duration-300 ease-in-out focus:ring-2 focus:ring-purple-300 focus:border-transparent" 
                    placeholder="Paste your text here..."
                ></textarea>
            </div>
            
            <button onClick={onUpload} className="flex items-center justify-center btn text-white bg-gradient-to-r from-purple-600 to-blue-500 hover:from-blue-500 hover:to-purple-600 transition duration-300 ease-in-out py-3 px-6 rounded-xl shadow-md">
                Submit
            </button>
        </div>
    );
}

export default LeftPanel;
