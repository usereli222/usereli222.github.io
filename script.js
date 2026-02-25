// Ambient Firefly Particle System
function createSpore() {
    const dustContainer = document.getElementById('ambient-dust');
    if (!dustContainer) return;

    const spore = document.createElement('div');
    spore.classList.add('spore');
    
    // Randomize size, position, and animation duration
    const size = Math.random() * 3 + 2; // Slightly smaller for fireflies
    const left = Math.random() * 100;
    const duration = Math.random() * 15 + 15; // Slower, lazier movement
    const delay = Math.random() * 5;

    spore.style.width = `${size}px`;
    spore.style.height = `${size}px`;
    spore.style.left = `${left}vw`;
    spore.style.animationDuration = `${duration}s`;
    spore.style.animationDelay = `${delay}s`;

    dustContainer.appendChild(spore);

    // Remove spore after animation completes to prevent DOM bloat
    setTimeout(() => {
        spore.remove();
    }, (duration + delay) * 1000);
}

// Initialize fireflies
setInterval(createSpore, 400);
for(let i=0; i<15; i++) createSpore(); // Initial burst

// Parallax Background Effect
document.addEventListener('mousemove', (e) => {
    const bg = document.querySelector('.world-bg');
    if (!bg) return;
    
    const x = e.clientX / window.innerWidth;
    const y = e.clientY / window.innerHeight;
    
    // Subtle movement
    bg.style.transform = `translate(-${x * 15}px, -${y * 15}px)`;
});

// Quest Interaction (Gamified Element)
document.addEventListener('DOMContentLoaded', () => {
    const quests = document.querySelectorAll('.quest-item');
    
    quests.forEach(quest => {
        quest.addEventListener('click', function() {
            if (this.classList.contains('active')) {
                this.classList.remove('active');
                this.classList.add('completed');
                
                // Optional: Add a little visual flair when completing
                const status = this.querySelector('.quest-status');
                status.style.transform = 'scale(1.2)';
                setTimeout(() => status.style.transform = 'scale(1)', 200);
            }
        });
    });

    // Profile Picture Cycler
    const profilePic = document.getElementById('profile-pic');
    if (profilePic) {
        // Add your own photo filenames here! Make sure they are in the 'images' folder.
        const photos = [
            //'images/hannahnme.jpeg',
            //'images/hehe.jpeg',
            //'images/meInNature.jpeg',
            'images/menpipi.jpeg',
            'images/smile.jpeg',
            'images/wideeyedpipi.jpeg'
        ];
        
        let currentPhotoIndex = 0;
        
        profilePic.addEventListener('click', () => {
            currentPhotoIndex = (currentPhotoIndex + 1) % photos.length;
            profilePic.src = photos[currentPhotoIndex];
        });
    }
});
