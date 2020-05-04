from games.models.games_session import HasRole

# def adopt_role(agent, role, session):
#     def create():
#         record = HasRole(
#             session_id=session,
#             agent_id=agent,
#             role_id=role,
#             is_active=True )
#         record.save()
#     return 