import json
import re

with open('order.html', 'r', encoding='utf-8') as f:
    order_html = f.read()

with open('scratch_menu_html.json', 'r', encoding='utf-8') as f:
    menu_html = json.load(f)['html']

# Update Title
order_html = order_html.replace('<title>Krishna Catering Services | Contact Us</title>', '<title>Krishna Catering Services | Order Form</title>')

# Update Page Header text
order_html = order_html.replace('<h1>Contact Us</h1>', '<h1>Place Your Order</h1>')
order_html = order_html.replace('<p>Let\'s plan your next memorable event together.</p>', '<p>Select your menu and customize your catering experience.</p>')

# Replace the contact grid layout with a single wide form layout
new_section = f'''
        <section class="order-section section" id="order">
            <div class="container">
                <div class="section-title center">
                    <span class="subtitle">Book Your Event</span>
                    <h2>Customize Your Menu</h2>
                    <p>Fill out the form below with your event details and select the items you'd like on your menu.</p>
                </div>
                
                <div class="order-form-container">
                    <form class="order-form" id="orderForm">
                        
                        <div class="form-section-title">
                            <h3>1. Event Details</h3>
                        </div>
                        <div class="form-grid-wide">
                            <div class="form-group">
                                <label>Full Name *</label>
                                <input type="text" id="orderName" placeholder="Your Full Name" required>
                            </div>
                            <div class="form-group">
                                <label>Phone Number *</label>
                                <input type="tel" id="orderPhone" placeholder="Phone Number" required>
                            </div>
                            <div class="form-group">
                                <label>Email Address</label>
                                <input type="email" id="orderEmail" placeholder="Email Address">
                            </div>
                            <div class="form-group">
                                <label>Event Date *</label>
                                <input type="date" id="orderDate" required>
                            </div>
                            <div class="form-group">
                                <label>Est. Guest Count *</label>
                                <input type="number" id="orderGuests" placeholder="Est. Guest Count" required>
                            </div>
                            <div class="form-group">
                                <label>Event Type *</label>
                                <select id="orderEventType" required>
                                    <option value="" disabled selected>Select Event Type</option>
                                    <option value="wedding">Wedding</option>
                                    <option value="corporate">Corporate Event</option>
                                    <option value="party">Private Party</option>
                                    <option value="other">Other</option>
                                </select>
                            </div>
                        </div>

                        <div class="form-section-title" style="margin-top: 3rem;">
                            <h3>2. Select Menu Items</h3>
                            <p class="text-muted" style="margin-bottom: 1.5rem;">Choose the items you want to include in your catering package.</p>
                        </div>
                        
                        <div class="menu-selection-container">
{menu_html}
                        </div>

                        <div class="form-section-title" style="margin-top: 3rem;">
                            <h3>3. Additional Requirements</h3>
                        </div>
                        <div class="form-group">
                            <textarea id="orderMessage" rows="4"
                                placeholder="Briefly describe any special requirements, allergies, or specific instructions..."></textarea>
                        </div>
                        <div style="text-align: center; margin-top: 2rem;">
                            <button type="submit" class="btn btn-primary btn-lg submit-btn" style="width: auto; padding: 1rem 3rem;">Submit Order Request <i
                                    class="fa-solid fa-paper-plane"></i></button>
                        </div>
                    </form>
                </div>
            </div>
        </section>
'''

order_html = re.sub(r'<!-- Contact Section -->.*?</section>', new_section, order_html, flags=re.DOTALL)

with open('order.html', 'w', encoding='utf-8') as f:
    f.write(order_html)

print('Updated order.html')
