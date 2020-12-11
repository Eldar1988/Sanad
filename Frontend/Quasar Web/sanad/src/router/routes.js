
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
    path: '/action/:slug',
    component: () => import('layouts/MainLayout.vue'),
    params: 'slug',
    children: [
      {path: '/action/:slug', component: () => import('pages/ActionDetail.vue')}
    ]
  },
  {
    path: '/actions',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {path: '/actions', component: () => import('pages/Actions.vue')}
    ]
  },
  {
    path: '/directions/:slug',
    component: () => import('layouts/MainLayout.vue'),
    params: 'slug',
    children: [
      {path: '/directions/:slug', component: () => import('pages/Directory.vue')}
    ]
  },
  {
    path: '/story/:slug',
    component: () => import('layouts/MainLayout.vue'),
    params: 'slug',
    children: [
      {path: '/story/:slug', component: () => import('pages/Story.vue')}
    ]
  },
  {
    path: '/doctor/:slug',
    component: () => import('layouts/MainLayout.vue'),
    params: 'slug',
    children: [
      {path: '/doctor/:slug', component: () => import('pages/Doctor.vue')}
    ]
  },
  {
    path: '/post/:slug',
    component: () => import('layouts/MainLayout.vue'),
    params: 'slug',
    children: [
      {path: '/post/:slug', component: () => import('pages/PostDetail.vue')}
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
