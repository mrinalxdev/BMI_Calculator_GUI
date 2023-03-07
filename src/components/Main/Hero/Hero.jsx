import React from 'react'

const Hero = () => {
  return (
    <div className="mt-[150px] text-center max-w-4xl m-auto">
      <h1 className="text-4xl font-bold font-['Lora'] pb-[10px]">The ultimate resource for developers of all levels. With us take your skills to the next level</h1>
      <p className="text-3xl font-bold font-['Lora']"><span>Build</span> and create the upcoming</p> 

      <div className="p-[40px]">
        <button className = "mr-9 px-10 py-2 bg-custom-green text-black rounded-xl font-semibold">Join</button>
        <button className = "ml-9 px-10 py-2 bg-custom-green text-black rounded-xl font-semibold">Explore More</button>
      </div>
    </div>
  )
}

export default Hero