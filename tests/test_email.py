import pytest
from unittest import mock
from app.services.email_service import EmailService
from app.utils.template_manager import TemplateManager

# Mailtrap in 11 ?
@pytest.mark.asyncio
async def test_send_markdown_email(email_service):
    user_data = {
        "email": "test@example.com",
        "name": "Test User",
        "verification_url": "http://example.com/verify?token=abc123"
    }
    with mock.patch.object(email_service, 'send_user_email') as mock_send_email:
        await email_service.send_user_email(user_data, 'email_verification')
        
        mock_send_email.asser_called_once_with(user_data, 'email_verification')
        
