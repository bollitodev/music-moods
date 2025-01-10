export default function Recommendation() {
    return (
        <div className="flex flex-nowrap justify-center gap-4 items-center">
            <h3 className="text-2xl font-bold text-center dark:text-white">
                Happy song for happy people
            </h3>

            <div class="flex justify-center items-center min-h-[300px] w-full">
                <card
                    class="bg-white w-full max-w-[768px] flex justify-start items-center p-8 relative max-h-40 shadow-sm rounded-md">
                    <img src="https://a10.gaanacdn.com/gn_img/albums/P7m3GvNKqx/7m3GVZx5Kq/size_l.jpg" class="rounded-xl w-[170px] mt-16"/>
                        <p class="pl-9 text-2xl font-semibold grow">
                            Roxette<br/><span class="text-lg font-normal">Sleeping in my car</span>
                        </p>
                        <span class="clear-left rounded-full bg-[#eff0f9] p-4 cursor-pointer group [&_*]:transition-all [&_*]:duration-150 [&_*]:ease-in">
                            <span class="px-3 py-3 block bg-white rounded-full shadow-md group-hover:bg-rose-600">
                                <svg xmlns="http://www.w3.org/2000/svg" class="group-hover:fill-white group-hover:stroke-white" width="28" height="28" viewBox="0 0 24 24" stroke-width="1.5" stroke="#7e9cff" fill="#7e9cff" stroke-linecap="round" stroke-linejoin="round">
                                    <path stroke="none" d="M0 0h24v24H0z" fill="none" />
                                    <path d="M7 4v16l13 -8z" />
                                </svg>
                            </span>
                        </span>
                </card>
            </div>
        </div>

            )
}