'use client';

import { useState } from 'react';

export default function AiMethodsPage() {
    const [text, setText] = useState('');
    const [summary, setSummary] = useState('');
    const [entities, setEntities] = useState([]);
    const [isLoading, setisLoading] = useState(false);
    const [isError, setisError] = useState(false);

    const handleSummarize = async () => {
        setisLoading(true);
        try {
            const response = await fetch('http://localhost:8000/api/summarize', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text })
            });

            const data = await response.json();
            setSummary(data.result);
            setisError(false);
        } catch (error) {
            console.error(error);
            setSummary("");
            setisError(true);
        } finally {
            setisLoading(false);
        }
    };

    const handleNER = async () => {
        setisLoading(true);
        try {
            const response = await fetch('http://localhost:8000/api/ner', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text })
            });
            const data = await response.json();

            setEntities(data.entities);
            setisError(false);
        } catch (error) {
            console.error(error);
            setEntities([]);
            setisError(true);
        } finally {
            setisLoading(false);
        }
    };

    return (
        <div className="flex flex-col items-center p-6 space-y-6">
            <textarea
                value={text}
                onChange={(e) => setText(e.target.value)}
                placeholder="Enter your text here..."
                className="w-full max-w-lg p-3 border rounded-md text-black"
            />
            <div className="flex space-x-4">
                <button onClick={handleSummarize} disabled={isLoading}>
                    Summarize
                </button>
                <button onClick={handleNER} disabled={isLoading}>
                    Extract Entities
                </button>
            </div>
            {isLoading && <div>Loading...</div>}
            {isError && <div>We are sorry there was an error. Try again later!</div>}
            {summary && (
                <div className="w-full max-w-lg p-4">
                    <div>
                        <h2 className="font-semibold">Summary:</h2>
                        <p>{summary}</p>
                    </div>
                </div>
            )}
            {entities.length > 0 && (
                <div className="w-full max-w-lg p-4">
                    <div>
                        <h2 className="font-semibold">Named Entities:</h2>
                        <ul className="list-disc pl-5">
                            {entities.map((entity, index) => (
                                <li key={index}>{entity.word} - <span className="text-blue-500">{entity.entity_group}</span></li>
                            ))}
                        </ul>
                    </div>
                </div>
            )}
        </div>
    );
}
