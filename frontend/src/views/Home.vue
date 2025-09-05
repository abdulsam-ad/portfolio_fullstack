<template>
  <section class="space-y-10">
    <!-- Hero Section -->
    <div class="bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500 text-white rounded-2xl shadow-xl p-10">
      <h1 class="text-4xl md:text-5xl font-extrabold mb-4">Shamas ulhaq</h1>
      <p class="text-lg mb-2">💻 Senior Software Engineer</p>
      <p class="mb-4">
        📍 Johar Town, Lahore · 📧
        <a href="mailto:ulhaqshams924@gmail.com" class="underline">
          ulhaqshams924@gmail.com
        </a>
        · 📞 03006785498
      </p>
      <a
        href="https://linkedin.com/in/shamas2772"
        target="_blank"
        class="bg-white text-indigo-600 font-semibold px-6 py-3 rounded-lg shadow hover:bg-gray-100 transition"
      >
        🌐 LinkedIn Profile
      </a>
      <a
        href="/Shamasulhaq-Resume.pdf"
        download
        class="ml-4 bg-yellow-400 text-black font-semibold px-6 py-3 rounded-lg shadow hover:bg-yellow-300 transition"
      >
        📄 Download Resume
      </a>
    </div>

    <!-- Profile Section -->
    <div class="bg-white rounded-2xl shadow p-8">
      <h2 class="text-3xl font-bold text-indigo-600 mb-4">✨ Profile</h2>
      <p class="text-gray-700 leading-relaxed">
        A seasoned Senior Software Engineer with a Bachelor's degree in Computer Science
        and extensive hands-on experience in Python, Django, and FastAPI. Proficient in
        developing scalable web applications and adept at creating RESTful APIs and
        microservices. Committed to delivering high-quality, maintainable code and exceeding
        client expectations through innovative and client-focused solutions.
      </p>
    </div>

    <!-- Skills Section -->
    <div class="bg-gradient-to-br from-green-400 via-teal-400 to-cyan-500 rounded-2xl shadow p-8 text-white">
      <h2 class="text-3xl font-bold mb-6">🛠 Skills</h2>
      <ul class="grid md:grid-cols-3 gap-3">
        <li class="bg-white/20 px-4 py-2 rounded-lg">Python / Django / FastAPI</li>
        <li class="bg-white/20 px-4 py-2 rounded-lg">Django REST Framework</li>
        <li class="bg-white/20 px-4 py-2 rounded-lg">Flask</li>
        <li class="bg-white/20 px-4 py-2 rounded-lg">PostgreSQL</li>
        <li class="bg-white/20 px-4 py-2 rounded-lg">Celery</li>
        <li class="bg-white/20 px-4 py-2 rounded-lg">Docker / AWS</li>
        <li class="bg-white/20 px-4 py-2 rounded-lg">Microservices</li>
        <li class="bg-white/20 px-4 py-2 rounded-lg">React / Redux / Angular</li>
        <li class="bg-white/20 px-4 py-2 rounded-lg">Agile Methodology</li>
      </ul>
    </div>

    <!-- Projects Section -->
    <div class="bg-white rounded-2xl shadow p-8">
      <h2 class="text-3xl font-bold text-pink-600 mb-6">🚀 Projects</h2>
      <div class="grid md:grid-cols-2 gap-6">
        <div class="p-6 bg-pink-100 rounded-xl shadow hover:shadow-lg transition">
          <h3 class="font-bold text-lg">NyNx Creatives</h3>
          <p class="text-gray-600">Freelancing platform with gigs, jobs, chat, payments, analytics.</p>
        </div>
        <div class="p-6 bg-indigo-100 rounded-xl shadow hover:shadow-lg transition">
          <h3 class="font-bold text-lg">ErisHROne</h3>
          <p class="text-gray-600">HR & account management system with advanced reporting.</p>
        </div>
        <div class="p-6 bg-yellow-100 rounded-xl shadow hover:shadow-lg transition">
          <h3 class="font-bold text-lg">Real Time Chat Bot</h3>
          <p class="text-gray-600">Django Channels + DRF for instant communication.</p>
        </div>
        <div class="p-6 bg-green-100 rounded-xl shadow hover:shadow-lg transition">
          <h3 class="font-bold text-lg">Gold Store Management</h3>
          <p class="text-gray-600">Automated inventory and transaction tracking system.</p>
        </div>
        <div class="p-6 bg-blue-100 rounded-xl shadow hover:shadow-lg transition">
          <h3 class="font-bold text-lg">Workerlot</h3>
          <p class="text-gray-600">Platform connecting workers with service providers.</p>
        </div>
      </div>
    </div>
  </section>
</template>
