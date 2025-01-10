import './App.css'
import Camera from './components/camera'
import Recommendation from './components/recommendation'

function App() {

  return (
    <div className='flex flex-col items-center justify-center h-screen bg-black'>
      <h1 className="mb-4 text-4xl font-extrabold leading-none tracking-tight text-gray-900 md:text-5xl lg:text-6xl dark:text-white">
        How do you feel today?
      </h1>
      <div>
        <Camera />
      </div>
      <div>
        <Recommendation />
      </div>
      
    </div>
  )
}

export default App
