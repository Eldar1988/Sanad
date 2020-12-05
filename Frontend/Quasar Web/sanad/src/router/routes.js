
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Index.vue') }
    ],
  },
  {
    path: '/about',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {path: '/about', component: () => import('pages/About.vue')}
    ]
  },
  {
    path: '/contacts',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {path: '/contacts', component: () => import('pages/Contacts.vue')}
    ]
  },
  {
    path: '/news',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {path: '/news', component: () => import('pages/News.vue')}
    ]
  },
  {
    path: '/actions',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {path: '/actions', component: () => import('pages/Actions.vue')}
    ]
  },
  // Always leave this as last one,
  // but you can also remove it
  {
    path: '*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
