import { CheckCircle2, Terminal, Code2, FileJson, FileText, Settings, Rocket } from "lucide-react";
import { motion } from "motion/react";

export default function App() {
  const steps = [
    { id: "01", name: "Requirements.txt", status: "completed" },
    { id: "02", name: ".env.example", status: "completed" },
    { id: "03", name: "LinkedIn_login.py", status: "completed" },
    { id: "04", name: "Scraper.py", status: "completed" },
    { id: "05", name: "Main.py", status: "completed" },
    { id: "06", name: "Readme.md", status: "completed" },
  ];

  const projectFiles = [
    { name: "main.py", size: "6kb" },
    { name: "scraper.py", size: "12kb", active: true },
    { name: "linkedin_login.py", size: "4kb" },
    { name: "output.csv", size: "244kb" },
    { name: "app.log", size: "1.2mb" },
  ];

  return (
    <div className="h-screen w-full bg-ivory text-charcoal font-sans flex flex-col overflow-hidden selection:bg-charcoal selection:text-ivory">
      {/* Header Navigation */}
      <nav className="border-b border-charcoal px-6 md:px-10 py-6 flex justify-between items-baseline">
        <div className="flex items-baseline gap-4">
          <h1 className="text-3xl md:text-4xl font-serif italic tracking-tight">Automation.eng</h1>
          <span className="hidden md:inline text-[10px] uppercase tracking-widest font-semibold text-[#666]">
            Sequence v2.04 — Build Phase
          </span>
        </div>
        <div className="flex gap-4 md:gap-8 text-[10px] md:text-[11px] uppercase tracking-[0.2em] font-medium">
          <span className="border-b border-charcoal cursor-pointer">Manifesto</span>
          <span className="opacity-40 hover:opacity-100 transition-opacity cursor-pointer">Architecture</span>
          <span className="opacity-40 hover:opacity-100 transition-opacity cursor-pointer">Environment</span>
        </div>
      </nav>

      {/* Main Content Grid */}
      <main className="flex-1 grid grid-cols-1 md:grid-cols-12 gap-0 overflow-hidden">
        
        {/* Left Column: Step & Index */}
        <section className="hidden md:flex col-span-3 border-r border-charcoal p-10 flex-col justify-between">
          <div>
            <div className="text-[120px] font-serif leading-none mb-4 -ml-2 select-none">04</div>
            <h2 className="text-xs uppercase tracking-[0.2em] font-bold mb-8 opacity-60 flex items-center gap-2">
              <Settings size={14} /> Current Task / Implementation
            </h2>
            <p className="font-serif italic text-2xl leading-relaxed mb-6">
              The Scraper Engine: Orchestrating Selenium to navigate the professional landscape.
            </p>
            <ul className="space-y-4 text-[11px] uppercase tracking-wider">
              {steps.map((step) => (
                <li 
                  key={step.id} 
                  className={`flex items-center gap-2 ${
                    step.status === 'completed' ? 'opacity-30 line-through' : step.id === '04' ? 'font-bold' : 'opacity-40'
                  }`}
                >
                  {step.id === '04' && <span className="mr-1">→</span>}
                  {step.id} {step.name}
                </li>
              ))}
            </ul>
          </div>
          
          <motion.div 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="bg-charcoal text-ivory p-6"
          >
            <div className="text-[9px] uppercase tracking-widest mb-4 opacity-60 flex items-center gap-2">
              <Terminal size={12} className="text-green-400" /> Live Kernel Status
            </div>
            <div className="font-mono text-[10px] space-y-1">
              <div className="text-green-400 flex items-center gap-2">
                <CheckCircle2 size={10} /> [DONE] Auth Module compiled
              </div>
              <motion.div 
                animate={{ opacity: [1, 0.5, 1] }}
                transition={{ repeat: Infinity, duration: 1.5 }}
                className="text-yellow-400 font-bold"
              >
                [EXEC] Writing scraper.py...
              </motion.div>
              <div className="opacity-40">[WAIT] Main loop pending</div>
            </div>
          </motion.div>
        </section>

        {/* Center Column: Code Aesthetics & File Preview */}
        <section className="col-span-1 md:col-span-6 p-6 md:p-12 border-r border-charcoal bg-sand overflow-y-auto">
          <div className="mb-10">
            <div className="flex justify-between items-end mb-4 border-b border-charcoal pb-2">
              <div className="flex items-center gap-2">
                <Code2 size={14} />
                <span className="font-mono text-xs text-charcoal">FILE: project/scraper.py</span>
              </div>
              <span className="text-[10px] uppercase tracking-widest">Line 142/480</span>
            </div>
            <div className="font-mono text-[12px] md:text-[13px] leading-relaxed text-[#444] bg-white p-6 md:p-8 border border-[#eee] shadow-sm overflow-x-auto whitespace-pre">
              <span className="text-blue-600">def</span> <span className="text-red-800">extract_profile_details</span>(driver, profile_url):<br/>
              &nbsp;&nbsp;&nbsp;&nbsp;<span className="text-gray-400"># Targeted extraction for 2024/2025 grads</span><br/>
              &nbsp;&nbsp;&nbsp;&nbsp;details = &#123;<br/>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span className="text-green-700">"Full Name"</span>: <span className="text-green-700">"N/A"</span>,<br/>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span className="text-green-700">"LinkedIn URL"</span>: profile_url,<br/>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span className="text-green-700">"College Name"</span>: <span className="text-green-700">"N/A"</span>,<br/>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span className="text-green-700">"Graduation Year"</span>: <span className="text-green-700">"N/A"</span><br/>
              &nbsp;&nbsp;&nbsp;&nbsp;&#125;<br/><br/>
              &nbsp;&nbsp;&nbsp;&nbsp;driver.get(profile_url)<br/>
              &nbsp;&nbsp;&nbsp;&nbsp;time.sleep(random.uniform(3, 5))
            </div>
          </div>
          
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-8">
            <div>
              <h3 className="text-[11px] font-bold uppercase tracking-widest mb-3 flex items-center gap-2">
                <FileJson size={14} /> Dependencies
              </h3>
              <div className="flex flex-wrap gap-2">
                {["SELENIUM", "PANDAS", "DOTENV", "WEBDRIVER-MGR"].map(dep => (
                  <span key={dep} className="px-2 py-1 border border-charcoal text-[9px] font-bold">
                    {dep}
                  </span>
                ))}
              </div>
            </div>
            <div className="sm:text-right">
              <h3 className="text-[11px] font-bold uppercase tracking-widest mb-3 flex items-center sm:justify-end gap-2">
                <Rocket size={14} /> Automation Stats
              </h3>
              <p className="text-3xl md:text-4xl font-serif">
                98.4<span className="text-sm italic">%</span>
              </p>
              <p className="text-[9px] uppercase opacity-60 tracking-tighter">Success Rate (Simulated Test)</p>
            </div>
          </div>
        </section>

        {/* Right Column: Meta & Logs */}
        <section className="hidden md:flex col-span-3 p-10 flex-col">
          <div className="mb-12">
            <h3 className="text-[11px] font-bold uppercase tracking-[0.2em] mb-6 pb-2 border-b border-charcoal flex items-center gap-2">
              <FileText size={14} /> Project Files
            </h3>
            <div className="space-y-2 font-mono text-[11px]">
              {projectFiles.map(file => (
                <div key={file.name} className={`flex justify-between ${file.active ? 'font-bold underline italic' : ''}`}>
                  <span>{file.name}</span>
                  <span className="opacity-40">{file.size}</span>
                </div>
              ))}
            </div>
          </div>

          <div className="flex-1 border-t border-charcoal pt-8 overflow-y-auto">
            <h3 className="text-[11px] font-bold uppercase tracking-[0.2em] mb-4">Methodology</h3>
            <div className="text-[11px] leading-relaxed text-[#666] italic">
              "The engine employs random exponential backoff to circumvent rate limiting. Each request is crafted to mimic organic navigation, systematically harvesting academic data from the professional graph while maintaining persistent session state."
            </div>
          </div>

          <div className="mt-auto">
            <div className="w-full h-1 bg-[#eee] mb-4 overflow-hidden">
              <motion.div 
                initial={{ width: "30%" }}
                animate={{ width: "68%" }}
                transition={{ duration: 2, ease: "easeInOut" }}
                className="h-full bg-charcoal"
              />
            </div>
            <div className="flex justify-between text-[10px] font-bold uppercase tracking-widest">
              <span>Deploy Progress</span>
              <span>68%</span>
            </div>
          </div>
        </section>

      </main>

      {/* Global Status Footer */}
      <footer className="border-t border-charcoal bg-charcoal text-ivory px-6 md:px-10 py-4 flex flex-col md:flex-row justify-between items-center gap-4 text-[10px] uppercase tracking-[0.3em] z-10">
        <div className="flex gap-6">
          <span>Session: LNK-99-ALPHA</span>
          <span className="text-green-400 flex items-center gap-1">
            <span className="animate-pulse">●</span> ACTIVE
          </span>
        </div>
        <div className="font-serif italic capitalize tracking-normal text-sm opacity-90 text-center">
          Python Automation Framework for Academic Research v1.0.1
        </div>
        <div className="text-[#666]">
          User: Expert_Audit_01
        </div>
      </footer>
    </div>
  );
}
