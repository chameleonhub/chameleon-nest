FROM node:14.19.2

ADD https://api.github.com/repos/road86/bahis-render-forms/git/refs/heads/develop version.json
RUN git clone https://github.com/road86/bahis-render-forms.git
ENV NODE_ENV=production
WORKDIR /bahis-render-forms
RUN npm install yarn
RUN yarn
CMD yarn start
