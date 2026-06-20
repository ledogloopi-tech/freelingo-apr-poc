from app.services.email_service import _render_template, _safe_html


def test_render_template_escapes_user_controlled_values():
    html = _render_template(
        "contact.html",
        {
            "email_title": "Contact",
            "logo": "FreeLingo",
            "from_label": "From",
            "subject_label": "Subject",
            "message_label": "Message",
            "sender_email": 'attacker@example.com"><img src=x onerror=alert(1)>',
            "subject": '<a href="https://phishing.example">Click</a>',
            "description": "<strong>urgent</strong> & dangerous",
            "footer": "Footer",
            "base_url": "https://freelingo.example",
        },
    )

    assert "<img src=x onerror=alert(1)>" not in html
    assert '<a href="https://phishing.example">Click</a>' not in html
    assert "<strong>urgent</strong>" not in html
    assert "&lt;img src=x onerror=alert(1)&gt;" in html
    assert "&lt;a href=&quot;https://phishing.example&quot;&gt;Click&lt;/a&gt;" in html
    assert "&lt;strong&gt;urgent&lt;/strong&gt; &amp; dangerous" in html


def test_render_template_preserves_explicitly_trusted_html():
    html = _render_template(
        "verify_email.html",
        {
            "greeting": "Hi Student,",
            "body": _safe_html("Welcome.<br /><strong>Verify now</strong>"),
            "button": "Verify",
            "link_fallback": "Copy this link:",
            "footer": "Footer",
            "url": "https://freelingo.example/verify-email?token=abc123",
            "base_url": "https://freelingo.example",
        },
    )

    assert "Welcome.<br /><strong>Verify now</strong>" in html
    assert "Welcome.&lt;br /&gt;&lt;strong&gt;Verify now&lt;/strong&gt;" not in html


def test_review_template_escapes_review_fields():
    html = _render_template(
        "review_submitted.html",
        {
            "email_title": "Review",
            "logo": "FreeLingo",
            "author_label": "Submitted by",
            "user_display_name": "<img src=x onerror=alert(1)>",
            "rating_label": "Rating",
            "rating": "5/5",
            "language_label": "Learning language",
            "target_language": "en-US",
            "comment_label": "Comment",
            "comment": '<a href="https://phishing.example">Click</a>',
            "cta": "View",
            "admin_url": "https://freelingo.example/admin/reviews",
            "footer": "Footer",
            "base_url": "https://freelingo.example",
        },
    )

    assert "<img src=x onerror=alert(1)>" not in html
    assert '<a href="https://phishing.example">Click</a>' not in html
    assert "&lt;img src=x onerror=alert(1)&gt;" in html
    assert "&lt;a href=&quot;https://phishing.example&quot;&gt;Click&lt;/a&gt;" in html
