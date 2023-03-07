import React from 'react'

const Navbar = () => {
  return (
    <div className = "flex justify-between items-center m-[30px]">
        <div className = "text-white text-3xl">
            {/* Logo  */}
            <h1>Dev<span className="font-bold cursor-pointer">Space</span></h1>
        </div>

        <div className="mr-6 text-[18px]">
            {/* NavItems  */}
            <a href="#" className = "text-white mr-[50px] ease-in-out duration-150 rounded-xl hover:border-none hover:p-3 hover:bg-custom-green hover:text-black">Explore</a>
            <a href="#" className = "text-white ml-[20px] ease-in-out duration-150 rounded-xl hover:border-none hover:p-3 hover:bg-custom-green hover:text-black">Sign In</a>
        </div>
    </div>
  )
}

export default Navbar