import { BrowserRouter, Routes, Route } from "react-router-dom"
import { useState } from "react"

import NewChat from "./components/NewChat"
import SideBar from "./components/SideBar"
import TopBar from "./components/TopBar"
import Conversation from "./components/Conversation"

function App() {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  return (
    <>
      <BrowserRouter>
        <div className=" md:grid md:grid-cols-6 h-svh w-screen text-sm overflow-hidden">
          <div className={`${mobileMenuOpen?"":"hidden"} absolute md:relative h-full md:flex md:col-span-1 z-10`}>
            <SideBar
              setMobileMenuOpen={setMobileMenuOpen}
            />
          </div>
          
          <div className="h-svh  md:col-span-5">
            <div className="flex h-1/10 w-full">
              <TopBar 
                setMobileMenuOpen={setMobileMenuOpen}
              />
            </div>
            <div className="h-9/10 z-0">
            <Routes>
              <Route path="/" element={<NewChat/>} />
              <Route path="/c/:conversationId" element ={<Conversation />} />
            </Routes>
            </div>
          </div>
        </div>
        
      </BrowserRouter>
    </>
  )
}

export default App
