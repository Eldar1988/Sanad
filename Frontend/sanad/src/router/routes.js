
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Index.vue') }
    ]
  },
  {
    path: '/doctors',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Doctors') }
    ]
  },
  {
    path: '/doctor/:slug',
    params: 'slug',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/DoctorDetail') }
    ]
  },
  {
    path: '/directions',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Directions') }
    ]
  },
  {
    path: '/direction/:slug',
    params: 'slug',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/DirectionDetail') }
    ]
  },
  {
    path: '/actions',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Actions') }
    ]
  },
  {
    path: '/action/:slug',
    params: 'slug',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/ActionDetail') }
    ]
  },
  {
    path: '/posts',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Posts') }
    ]
  },
  {
    path: '/post/:slug',
    params: 'slug',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/PostDetail') }
    ]
  },
  {
    path: '/stories',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Stories') }
    ]
  },
  {
    path: '/story/:slug',
    params: 'slug',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/StoryDetail') }
    ]
  },
  {
    path: '/reviews',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Reviews/Reviews') }
    ]
  },
  {
    path: '/review/:id',
    params: 'id',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Reviews/ReviewDetail') }
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
