css_to_append = """

/* --- Order Form Styles --- */
.order-section {
    padding-top: 2rem;
}

.order-form-container {
    background: var(--bg-card);
    padding: 3rem;
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow-md);
    max-width: 1000px;
    margin: 0 auto;
}

.form-section-title {
    margin-bottom: 1.5rem;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid var(--border-color);
}

.form-section-title h3 {
    font-size: 1.5rem;
    color: var(--text-dark);
}

.form-grid-wide {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1.5rem;
    margin-bottom: 2rem;
}

.form-group label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: 500;
    color: var(--text-dark);
}

.menu-selection-container {
    display: flex;
    flex-direction: column;
    gap: 2.5rem;
    margin-bottom: 2rem;
}

.menu-category h4 {
    font-family: var(--font-heading);
    font-size: 1.3rem;
    color: var(--primary-color);
    margin-bottom: 1rem;
    position: relative;
    padding-left: 1rem;
}

.menu-category h4::before {
    content: '';
    position: absolute;
    left: 0;
    top: 50%;
    transform: translateY(-50%);
    width: 4px;
    height: 100%;
    background-color: var(--primary-color);
    border-radius: 2px;
}

.checkbox-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 1rem;
}

.checkbox-label {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    cursor: pointer;
    font-size: 0.95rem;
    color: var(--text-light);
    transition: var(--transition);
}

.checkbox-label:hover {
    color: var(--primary-color);
}

.checkbox-label input[type="checkbox"] {
    appearance: none;
    background-color: var(--bg-light);
    margin: 0;
    font: inherit;
    color: currentColor;
    width: 1.15em;
    height: 1.15em;
    border: 2px solid var(--border-color);
    border-radius: 0.15em;
    display: grid;
    place-content: center;
    transition: var(--transition);
}

.checkbox-label input[type="checkbox"]::before {
    content: "";
    width: 0.65em;
    height: 0.65em;
    transform: scale(0);
    transition: 120ms transform ease-in-out;
    box-shadow: inset 1em 1em var(--bg-card);
    background-color: var(--primary-color);
    transform-origin: bottom left;
    clip-path: polygon(14% 44%, 0 65%, 50% 100%, 100% 16%, 80% 0%, 43% 62%);
}

.checkbox-label input[type="checkbox"]:checked {
    background-color: var(--primary-color);
    border-color: var(--primary-color);
}

.checkbox-label input[type="checkbox"]:checked::before {
    transform: scale(1);
}

@media (max-width: 768px) {
    .form-grid-wide {
        grid-template-columns: 1fr;
    }
    
    .order-form-container {
        padding: 1.5rem;
    }
    
    .checkbox-grid {
        grid-template-columns: 1fr 1fr;
    }
}
@media (max-width: 480px) {
    .checkbox-grid {
        grid-template-columns: 1fr;
    }
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_to_append)

print("CSS appended to style.css")
