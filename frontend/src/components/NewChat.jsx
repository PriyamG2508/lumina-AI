import { IoSend } from "react-icons/io5";

export default function NewChat(){
    return (
        <>
            <div className="h-full">
                <div className="flex flex-col h-full p-10 gap-4 items-center justify-center">
                    <div className="flex text-xl sm:text-2xl font-semibold tracking-tighter justify-center ">What's on your mind today?</div>
                    <div className="flex p-4 mx-auto max-w-2xl w-full overflow-hidden">
                        <div className="flex flex-col px-4 py-2 w-2xl h-fit border border-gray-500 rounded-3xl shadow-lg shadow-gray-300">
                            <textarea
                                placeholder="Type your message here..."
                                className="flex flex-row focus:outline-none w-full resize-none overflow-hidden"
                                onInput={(e) => {
                                    e.target.style.height = 'auto';
                                    e.target.style.height = e.target.scrollHeight + 'px';
                                }}
                                rows={1}
                            />
                            <div className="flex justify-end">
                                <IoSend className="text-2xl cursor-pointer hover:text-gray-800" />
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </>
    );
}