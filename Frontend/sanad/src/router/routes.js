
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
      { path: '', component: () => import('pages/Doctors/Doctors') }
    ]
  },
  {
    path: '/doctor/:slug',
    params: 'slug',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Doctors/DoctorDetail') }
    ]
  },
  {
    path: '/directions',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Directions/Directions') }
    ]
  },
  {
    path: '/direction/:slug',
    params: 'slug',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Directions/DirectionDetail') }
    ]
  },
  {
    path: '/actions',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Actions/Actions') }
    ]
  },
  {
    path: '/action/:slug',
    params: 'slug',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Actions/ActionDetail') }
    ]
  },
  {
    path: '/posts',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Posts/Posts') }
    ]
  },
  {
    path: '/post/:slug',
    params: 'slug',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Posts/PostDetail') }
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
      {
        path: '',
        component: () => import('pages/Reviews/Reviews')
      },
      {
        path: ':id',
        component: () => import('layouts/MainLayout.vue'),
        children: [
          { path: '', component: () => import('pages/Reviews/ReviewDetail') }
        ]
      },
    ]
  },

  {
    path: '/videos',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/About/Videos') }
    ]
  },
  {
    path: '/about',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/About/About') }
    ]
  },
  {
    path: '/price',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Price') }
    ]
  },
  {
    path: '/info-page',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: ':slug', name: 'info-page', component: () => import('pages/InfoPage') }
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
