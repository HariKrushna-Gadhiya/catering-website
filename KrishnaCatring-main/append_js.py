js_to_append = """
    // 6. Order Form Submission via EmailJS
    const orderForm = document.getElementById('orderForm');
    if (orderForm) {
        orderForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const submitBtn = orderForm.querySelector('button[type="submit"]');
            const originalText = submitBtn.innerHTML;

            submitBtn.innerHTML = '<i class="fa-solid fa-circle-notch fa-spin"></i> Submitting...';
            submitBtn.style.opacity = '0.8';
            submitBtn.disabled = true;

            // Get form values
            const name = document.getElementById('orderName').value;
            const phone = document.getElementById('orderPhone').value;
            const email = document.getElementById('orderEmail').value;
            const date = document.getElementById('orderDate').value;
            const guests = document.getElementById('orderGuests').value;
            const eventType = document.getElementById('orderEventType').value;
            const message = document.getElementById('orderMessage').value;

            // Get selected menu items
            const checkboxes = document.querySelectorAll('input[name="menu_items"]:checked');
            let selectedItems = [];
            checkboxes.forEach((cb) => {
                selectedItems.push(cb.value);
            });
            const menuItemsText = selectedItems.length > 0 ? selectedItems.join(', ') : 'None selected';

            // --- EmailJS Integration ---
            const emailjsServiceId = 'service_ccj2qeg';
            const emailjsTemplateId = 'template_xzlr2ec';
            const emailjsPublicKey = 'FRHDhJ4nDOT9wwXpQ';

            try {
                const combinedMessage = `Selected Menu Items:\\n${menuItemsText}\\n\\nAdditional Requirements:\\n${message}`;
                
                const templateParams = {
                    subject: 'New Catering Order',
                    name: name,
                    email: email || 'Not provided',
                    phone: phone,
                    date: date,
                    guests: guests,
                    eventType: eventType,
                    message: combinedMessage
                };

                if (window.emailjs) {
                    emailjs.init(emailjsPublicKey);
                    await emailjs.send(emailjsServiceId, emailjsTemplateId, templateParams);
                    
                    submitBtn.innerHTML = '<i class="fa-solid fa-check"></i> Sent Successfully';
                    submitBtn.style.backgroundColor = '#2a9d8f';
                    submitBtn.style.color = '#fff';
                    
                    setTimeout(() => {
                        alert('Order request sent successfully! We will contact you soon.');
                        orderForm.reset();
                    }, 500);
                } else {
                    throw new Error("EmailJS not loaded");
                }
                
            } catch (error) {
                console.error("Submission Error:", error);
                submitBtn.innerHTML = '<i class="fa-solid fa-xmark"></i> Failed to send';
                submitBtn.style.backgroundColor = '#e76f51';
                submitBtn.style.color = '#fff';
                alert("Sorry, there was an error submitting your request. Please try contacting us directly via phone.");
            } finally {
                setTimeout(() => {
                    submitBtn.innerHTML = originalText;
                    submitBtn.style.backgroundColor = '';
                    submitBtn.style.opacity = '1';
                    submitBtn.disabled = false;
                }, 3000);
            }
        });
    }
"""

with open('script.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the last `});` with the new logic + `});`
if content.endswith('});\\n'):
    content = content[:-4] + js_to_append + '\\n});\\n'
elif content.endswith('});'):
    content = content[:-3] + js_to_append + '\\n});'

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("JS injected into script.js")
