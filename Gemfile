source 'https://rubygems.org'

group :jekyll_plugins do
  # 固定 Jekyll 4.3.2 精确版本（Windows Ruby 3.1 已验证兼容）
  gem 'jekyll', '4.3.2'
  # jekyll-sass-converter 3.x 使用 sass-embedded（有 x64-mingw-ucrt 预编译二进制，无需本地编译）
  gem 'jekyll-sass-converter', '~> 3.0'
  gem 'jekyll-feed', '~> 0.16'
  gem 'jekyll-sitemap', '~> 1.4'
  gem 'jekyll-redirect-from', '~> 0.16'
  gem 'jekyll-gist'
  gem 'jekyll-paginate'
  # jemoji 注释掉（C 扩展在 Ruby 3.1 下编译失败）
  # gem 'jemoji'
  gem 'webrick'
end

# Windows 兼容必备
gem 'tzinfo-data', platforms: [:mswin, :mingw, :x64_mingw]
gem 'connection_pool', '~> 2.5'

# 固定 google-protobuf 使用 ~> 4.30（sass-embedded 兼容）
# 同时固定 sass-embedded 在不要求 bigdecimal 4.x 的版本范围内
gem 'sass-embedded', '~> 1.86.0'
gem 'google-protobuf', '~> 4.30.2'

# 锁死 bigdecimal 到 Ruby 3.1 内置版本，阻止 bundle 升级到需要 C 编译的 4.x
gem 'bigdecimal', '3.1.1'
