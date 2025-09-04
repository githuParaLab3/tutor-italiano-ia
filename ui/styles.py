# ui/styles.py

custom_css = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Poppins:wght@400;500;600;700&display=swap');
body { background: #f0f2f5; font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; }
.gradio-container { background: #ffffff; border-radius: 16px; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08); }
.main-heading { font-family: 'Poppins', sans-serif !important; font-size: 3rem !important; font-weight: 700 !important; color: #34495e; text-align: center !important; margin: 20px 0 10px 0 !important; }
.sub-heading { text-align: center !important; color: #64748b !important; font-size: 1.2rem !important; font-weight: 500 !important; margin: 0 0 30px 0 !important; opacity: 0.9 !important; }
.tabs { border-radius: 12px; }
.gradio-tabs-nav button { font-weight: 600; font-family: 'Poppins', sans-serif !important; color: #34495e; transition: all 0.3s ease; }
.gradio-tabs-nav button.selected { color: #4c51bf; border-bottom: 2px solid #4c51bf; background: rgba(76, 81, 191, 0.05); }
.quick-tools-section { background: #fafafa !important; border: 1px solid #e0e0e0 !important; border-radius: 20px !important; padding: 32px !important; margin: 16px !important; transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important; box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05) !important; }
.quick-tools-section:hover { transform: translateY(-5px) !important; box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1) !important; }
.tool-heading { font-family: 'Poppins', sans-serif !important; color: #2d3748 !important; font-size: 1.4rem !important; font-weight: 600 !important; padding-bottom: 8px !important; margin-bottom: 20px !important; border-bottom: 2px solid #e2e8f0; }
.button-primary { background: linear-gradient(135deg, #4c51bf, #667eea) !important; color: white !important; font-weight: 600 !important; border: none !important; border-radius: 14px !important; padding: 14px 28px !important; cursor: pointer !important; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important; box-shadow: 0 4px 15px rgba(79, 70, 229, 0.4) !important; text-transform: uppercase !important; letter-spacing: 0.5px !important; }
.button-primary:hover { transform: translateY(-3px) !important; box-shadow: 0 8px 25px rgba(79, 70, 229, 0.5) !important; }
.gr-button-secondary { background: #f8fafc !important; border: 2px solid #e2e8f0 !important; color: #4a5568 !important; border-radius: 12px !important; font-weight: 500 !important; transition: all 0.3s ease !important; }
.gr-button-secondary:hover { background: #e2e8f0 !important; transform: translateY(-2px) !important; }
.gr-chatbot { border-radius: 20px !important; border: 1px solid #e2e8f0 !important; background: #ffffff !important; }
.gr-textbox { border-radius: 14px !important; border: 2px solid #e2e8f0 !important; background: #ffffff !important; transition: all 0.3s ease !important; padding: 16px !important; }
.gr-textbox:focus { border-color: #4c51bf !important; box-shadow: 0 0 0 4px rgba(79, 70, 229, 0.1) !important; transform: translateY(-1px) !important; }
.gr-chatbot .user-message { background-color: #e3f2fd; border-radius: 15px 15px 0 15px; color: #1a237e; font-weight: 500; }
.gr-chatbot .bot-message { background-color: #e8f5e9; border-radius: 15px 15px 15px 0; color: #1b5e20; font-weight: 500; }
"""