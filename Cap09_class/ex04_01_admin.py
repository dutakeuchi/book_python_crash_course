# %%
from user_privilege import Admin
# %%
new_admin = Admin('john','ken',35,'brazilian','a+')
new_admin.info_user()
# %%
new_admin.privilege.add_privilege(['delete post','edit post'])
new_admin.privilege.show_privileges()
# %%
new_admin.info_user()
# %%
