<html>
<body>
<!--StartFragment--><h2 data-start="346" data-end="415"> Image-based Breed Recognition for Cattle and Buffaloes of India</h2>
<h3 data-start="417" data-end="432">📘 Overview</h3>
<p data-start="433" data-end="798">This project focuses on building an AI-based system that can automatically recognize and classify <strong data-start="531" data-end="567">Indian cattle and buffalo breeds</strong> from images.<br data-start="580" data-end="583">
Using <strong data-start="589" data-end="606">Deep Learning</strong> and <strong data-start="611" data-end="630">Computer Vision</strong> techniques, this model helps in identifying breeds such as Gir, Sahiwal, Murrah, Tharparkar, and others — supporting farmers, veterinarians, and livestock researchers.</p>
<hr data-start="800" data-end="803">
<h3 data-start="805" data-end="822">🎯 Objectives</h3>
<ul data-start="823" data-end="1168">
<li data-start="823" data-end="906">
<p data-start="825" data-end="906">Develop an <strong data-start="836" data-end="866">image classification model</strong> for Indian cattle and buffalo breeds.</p>
</li>
<li data-start="907" data-end="974">
<p data-start="909" data-end="974">Build a <strong data-start="917" data-end="928">dataset</strong> of labeled images for training and testing.</p>
</li>
<li data-start="975" data-end="1092">
<p data-start="977" data-end="1092">Implement a <strong data-start="989" data-end="1027">Convolutional Neural Network (CNN)</strong> or transfer learning model (like ResNet, VGG16, or MobileNet).</p>
</li>
<li data-start="1093" data-end="1168">
<p data-start="1095" data-end="1168">Deploy the model as a simple <strong data-start="1124" data-end="1154">web or desktop application</strong> for easy use.</p>
</li>
</ul>
<hr data-start="1170" data-end="1173">
<h3 data-start="1175" data-end="1199">📂 Project Structure</h3>
<pre class="overflow-visible!" data-start="1200" data-end="1554"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>📦 Image-Breed-Recognition
├── 📁 dataset/
│   ├── cattle/
│   ├── buffalo/
│   └── labels.csv
├── 📁 models/
│   ├── model_cnn.h5
│   ├── model_resnet50.h5
├── 📁 notebooks/
│   ├── data_preprocessing.ipynb
│   ├── model_training.ipynb
├── 📁 app/
│   ├── main.py
│   ├── templates/
│   └── </span><span><span class="hljs-type">static</span></span><span>/
├── requirements.txt
├── README.md
└── LICENSE
</span></span></code></div></div></pre>
<hr data-start="1556" data-end="1559">
<h3 data-start="1561" data-end="1585">🧠 Technologies Used</h3>
<ul data-start="1586" data-end="1732">
<li data-start="1586" data-end="1604">
<p data-start="1588" data-end="1604"><strong data-start="1588" data-end="1604">Python 3.10+</strong></p>
</li>
<li data-start="1605" data-end="1629">
<p data-start="1607" data-end="1629"><strong data-start="1607" data-end="1629">TensorFlow / Keras</strong></p>
</li>
<li data-start="1630" data-end="1642">
<p data-start="1632" data-end="1642"><strong data-start="1632" data-end="1642">OpenCV</strong></p>
</li>
<li data-start="1643" data-end="1663">
<p data-start="1645" data-end="1663"><strong data-start="1645" data-end="1663">NumPy &amp; Pandas</strong></p>
</li>
<li data-start="1664" data-end="1690">
<p data-start="1666" data-end="1690"><strong data-start="1666" data-end="1690">Matplotlib / Seaborn</strong></p>
</li>
<li data-start="1691" data-end="1732">
<p data-start="1693" data-end="1732"><strong data-start="1693" data-end="1732">Flask or Streamlit (for deployment)</strong></p>
</li>
</ul>
<hr data-start="1734" data-end="1737">
<h3 data-start="1739" data-end="1758">⚙️ Installation</h3>
<pre class="overflow-visible!" data-start="1759" data-end="1991"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span><span class="hljs-comment"># Clone this repository</span></span><span>
git </span><span><span class="hljs-built_in">clone</span></span><span> https://github.com/&lt;your-username&gt;/Image-Breed-Recognition.git

</span><span><span class="hljs-comment"># Navigate into the project folder</span></span><span>
</span><span><span class="hljs-built_in">cd</span></span><span> Image-Breed-Recognition

</span><span><span class="hljs-comment"># Install required packages</span></span><span>
pip install -r requirements.txt
</span></span></code></div></div></pre>
<hr data-start="1993" data-end="1996">
<h3 data-start="1998" data-end="2010">🚀 Usage</h3>
<pre class="overflow-visible!" data-start="2011" data-end="2063"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span><span class="hljs-comment"># Run the application</span></span><span>
python app/main.py
</span></span></code></div></div></pre>
<p data-start="2064" data-end="2095">Or, if you are using Streamlit:</p>
<pre class="overflow-visible!" data-start="2096" data-end="2133"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>streamlit run app/main.py
</span></span></code></div></div></pre>
<p data-start="2135" data-end="2243">Upload an image of a <strong data-start="2156" data-end="2177">cattle or buffalo</strong>, and the model will predict the breed with confidence percentage.</p>
<hr data-start="2245" data-end="2248">
<h3 data-start="2250" data-end="2271">🧩 Model Training</h3>
<ul data-start="2272" data-end="2459">
<li data-start="2272" data-end="2335">
<p data-start="2274" data-end="2335">Image preprocessing using OpenCV and augmentation techniques.</p>
</li>
<li data-start="2336" data-end="2389">
<p data-start="2338" data-end="2389">Transfer learning using <strong data-start="2362" data-end="2388">ResNet50 / MobileNetV2</strong>.</p>
</li>
<li data-start="2390" data-end="2459">
<p data-start="2392" data-end="2459">Evaluation using accuracy, precision, recall, and confusion matrix.</p>
</li>
</ul>
<hr data-start="2461" data-end="2464">
<h3 data-start="2466" data-end="2480">📊 Results</h3>
<div class="_tableContainer_1rjym_1"><div tabindex="-1" class="group _tableWrapper_1rjym_13 flex w-fit flex-col-reverse">
Model | Accuracy | Dataset Used
-- | -- | --
CNN (Custom) | 85.4% | 2000 images
ResNet50 | 93.2% | 2000 images
MobileNetV2 | 94.1% | 2000 images

</div></div>
<hr data-start="2668" data-end="2671">
<h3 data-start="2673" data-end="2692">💡 Future Scope</h3>
<ul data-start="2693" data-end="2891">
<li data-start="2693" data-end="2733">
<p data-start="2695" data-end="2733">Increase dataset size and diversity.</p>
</li>
<li data-start="2734" data-end="2781">
<p data-start="2736" data-end="2781">Add <strong data-start="2740" data-end="2778">real-time camera-based recognition</strong>.</p>
</li>
<li data-start="2782" data-end="2830">
<p data-start="2784" data-end="2830">Integrate with <strong data-start="2799" data-end="2813">mobile app</strong> for field use.</p>
</li>
<li data-start="2831" data-end="2891">
<p data-start="2833" data-end="2891">Include <strong data-start="2841" data-end="2862">disease detection</strong> alongside breed recognition.</p>
</li>
</ul>
<hr data-start="2893" data-end="2896">
<h3 data-start="2898" data-end="2920">👨‍💻 Contributors</h3>
<ul data-start="2921" data-end="2996">
<li data-start="2921" data-end="2962">
<p data-start="2923" data-end="2962"><strong data-start="2923" data-end="2945">Dinesh Kumar Yadav</strong> – Project Lead</p>
</li>
<li data-start="2963" data-end="2996">
<p data-start="2965" data-end="2996">[RIVEN]</p>
<p data-start="2965" data-end="2996">MY TEAM MEMBERS  ---->     1.Raj Ritik Varma   2. Aman Yadav  3. Piyush Asthana  4,  Janhavi Tiwari  5. Garima Singh</p>

</li>
</ul>
<hr data-start="2998" data-end="3001">
<h3 data-start="3003" data-end="3017">📜 License</h3>
<p data-start="3018" data-end="3112">This project is licensed under the <strong data-start="3053" data-end="3068">MIT License</strong> – feel free to use, modify, and distribute.</p>
<hr data-start="3114" data-end="3117">
<h3 data-start="3119" data-end="3140">⭐ Acknowledgments</h3>
<p data-start="3141" data-end="3159">Special thanks to:</p>
<ul data-start="3160" data-end="3292">
<li data-start="3160" data-end="3229">
<p data-start="3162" data-end="3229">ICAR (Indian Council of Agricultural Research) for breed datasets</p>
</li>
<li data-start="3230" data-end="3292">
<p data-start="3232" data-end="3292">Open-source contributors in TensorFlow &amp; PyTorch community</p></li></ul><!--EndFragment-->
</body>
</html>
