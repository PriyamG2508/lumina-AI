import { LuSquarePen } from "react-icons/lu";
import { RxCross2 } from "react-icons/rx";

const chatList = [
    { name: "Chat 1" },
    { name: "Chat 2" },
    { name: "Chat 3" },
    { name: "Chat 4" }
];
export default function SideBar({setMobileMenuOpen}){
    return (
        <>
            <div className="flex flex-col gap-1 w-fit md:w-full h-full p-2 border border-gray-200 bg-gray-50  opacity-100">
                <div className="flex md:hidden justify-between items-center gap-30 px-2">
                    <h1 className="text-2xl font-semibold tracking-tighter">Lumina</h1>
                    <RxCross2 
                        className="text-2xl cursor-pointer"
                        onClick={()=>setMobileMenuOpen(false)}
                    />
                </div>
                <div className="flex gap-2 items-center hover:bg-gray-200 p-2 rounded-xl cursor-pointer">
                    <LuSquarePen className="text-lg" />
                    <div>New chat</div>
                </div>
                <div className="text-gray-400 p-2">Chats</div>
                <div className="flex flex-col">
                    {chatList.map((chat, index) => (
                        <div key={index} className="flex gap-2 items-center hover:bg-gray-200 p-2 rounded-xl cursor-pointer">
                            {chat.name}
                        </div>
                    ))}
                </div>
            </div>
        </>
    );
}