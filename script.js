// Theme toggle (keeps simple preference in localStorage)
function toggleMode() {
    document.body.classList.toggle('dark');
    try { localStorage.setItem('prefersDark', document.body.classList.contains('dark')); } catch (e) {}
}

// Apply saved preference on load
(function () {
    try {
        const pref = localStorage.getItem('prefersDark');
        if (pref === 'true') document.body.classList.add('dark');
    } catch (e) {}
})();

